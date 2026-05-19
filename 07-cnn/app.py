"""
Flask inference API + web UI for the MNIST digit recognition model.

Run:
    pip install -r ../requirements.txt
    python app.py

Then open http://localhost:5000
"""

import base64
import io
import os

import numpy as np
from flask import Flask, jsonify, render_template, request
from PIL import Image, ImageOps
from tensorflow import keras

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "mnist_cnn_model.keras")

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)

_model = None


def get_model():
    global _model
    if _model is None:
        _model = keras.models.load_model(MODEL_PATH)
    return _model


def decode_data_url(data_url: str) -> Image.Image:
    header, _, b64data = data_url.partition(",")
    raw = base64.b64decode(b64data)
    return Image.open(io.BytesIO(raw))


def preprocess(img: Image.Image, invert: bool) -> tuple[np.ndarray, str]:
    """Convert PIL image to normalized 28x28 model input, MNIST-style.

    Pipeline:
      1. Grayscale.
      2. Invert if needed so digit is light-on-dark.
      3. Threshold to suppress noise.
      4. Crop bounding box of foreground pixels.
      5. Resize keeping aspect so longest side is 20 px.
      6. Paste centered into a 28x28 black canvas (MNIST convention).
    Returns (model_input_tensor, preview_data_url).
    """
    img = img.convert("L")
    if invert:
        img = ImageOps.invert(img)

    arr = np.array(img, dtype=np.uint8)

    # Adaptive threshold: anything above 20% of max is foreground.
    fg_threshold = max(40, int(arr.max() * 0.25))
    mask = arr > fg_threshold

    if not mask.any():
        # Empty image — return blank 28x28.
        canvas = np.zeros((28, 28), dtype=np.float32)
    else:
        rows = np.where(mask.any(axis=1))[0]
        cols = np.where(mask.any(axis=0))[0]
        top, bottom = rows[0], rows[-1] + 1
        left, right = cols[0], cols[-1] + 1
        cropped = arr[top:bottom, left:right]

        # Zero-out below-threshold pixels (removes gray noise from photos).
        cropped = np.where(cropped > fg_threshold, cropped, 0).astype(np.uint8)

        h, w = cropped.shape
        scale = 20.0 / max(h, w)
        new_w = max(1, int(round(w * scale)))
        new_h = max(1, int(round(h * scale)))
        resized = Image.fromarray(cropped).resize((new_w, new_h), Image.LANCZOS)

        canvas_img = Image.new("L", (28, 28), 0)
        offset_x = (28 - new_w) // 2
        offset_y = (28 - new_h) // 2
        canvas_img.paste(resized, (offset_x, offset_y))
        canvas = np.array(canvas_img, dtype=np.float32) / 255.0

    tensor = canvas.reshape(1, 28, 28, 1)

    buf = io.BytesIO()
    Image.fromarray((canvas * 255).astype("uint8")).resize(
        (140, 140), Image.NEAREST
    ).save(buf, format="PNG")
    preview = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()

    return tensor, preview


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/predict", methods=["POST"])
def predict():
    payload = request.get_json(silent=True) or {}
    image_data = payload.get("image")
    source = payload.get("source", "canvas")

    if not image_data:
        return jsonify({"error": "Missing 'image' field (base64 data URL)."}), 400

    try:
        img = decode_data_url(image_data)
    except Exception as exc:
        return jsonify({"error": f"Could not decode image: {exc}"}), 400

    invert = source == "upload"
    tensor, preview = preprocess(img, invert=invert)

    proba = get_model().predict(tensor, verbose=0)[0]
    proba_list = proba.astype(float).tolist()

    ranked = sorted(enumerate(proba_list), key=lambda kv: kv[1], reverse=True)
    top3 = [{"digit": int(d), "confidence": float(p)} for d, p in ranked[:3]]

    return jsonify({
        "prediction": int(ranked[0][0]),
        "confidence": float(ranked[0][1]),
        "probabilities": proba_list,
        "top3": top3,
        "preview": preview,
    })


@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "model_loaded": _model is not None})


if __name__ == "__main__":
    get_model()
    app.run(host="0.0.0.0", port=5000, debug=False)
