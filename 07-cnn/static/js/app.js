(() => {
    const $ = (sel) => document.querySelector(sel);
    const $$ = (sel) => Array.from(document.querySelectorAll(sel));

    // ===== Theme =====
    const themeKey = "mnist-app-theme";
    const savedTheme = localStorage.getItem(themeKey);
    if (savedTheme) document.documentElement.setAttribute("data-theme", savedTheme);
    $("#theme-toggle").addEventListener("click", () => {
        const next = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
        document.documentElement.setAttribute("data-theme", next);
        localStorage.setItem(themeKey, next);
    });

    // ===== Tabs =====
    $$(".tab").forEach((tab) => {
        tab.addEventListener("click", () => {
            $$(".tab").forEach((t) => {
                t.classList.remove("active");
                t.setAttribute("aria-selected", "false");
            });
            tab.classList.add("active");
            tab.setAttribute("aria-selected", "true");
            const target = tab.dataset.tab;
            $$(".tab-panel").forEach((p) => p.classList.toggle("active", p.dataset.panel === target));
        });
    });

    // ===== Canvas =====
    const canvas = $("#canvas");
    const ctx = canvas.getContext("2d", { willReadFrequently: true });
    let drawing = false;
    let strokeWidth = 20;
    let lastPos = null;

    const clearCanvas = () => {
        ctx.fillStyle = "#000000";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    };
    clearCanvas();

    const getPos = (evt) => {
        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;
        const point = evt.touches ? evt.touches[0] : evt;
        return {
            x: (point.clientX - rect.left) * scaleX,
            y: (point.clientY - rect.top) * scaleY,
        };
    };

    const startDraw = (evt) => {
        evt.preventDefault();
        drawing = true;
        lastPos = getPos(evt);
        ctx.beginPath();
        ctx.arc(lastPos.x, lastPos.y, strokeWidth / 2, 0, Math.PI * 2);
        ctx.fillStyle = "#ffffff";
        ctx.fill();
    };
    const moveDraw = (evt) => {
        if (!drawing) return;
        evt.preventDefault();
        const pos = getPos(evt);
        ctx.strokeStyle = "#ffffff";
        ctx.lineWidth = strokeWidth;
        ctx.lineCap = "round";
        ctx.lineJoin = "round";
        ctx.beginPath();
        ctx.moveTo(lastPos.x, lastPos.y);
        ctx.lineTo(pos.x, pos.y);
        ctx.stroke();
        lastPos = pos;
    };
    const endDraw = () => { drawing = false; lastPos = null; };

    canvas.addEventListener("mousedown", startDraw);
    canvas.addEventListener("mousemove", moveDraw);
    canvas.addEventListener("mouseup", endDraw);
    canvas.addEventListener("mouseleave", endDraw);
    canvas.addEventListener("touchstart", startDraw, { passive: false });
    canvas.addEventListener("touchmove", moveDraw, { passive: false });
    canvas.addEventListener("touchend", endDraw);

    $("#stroke-width").addEventListener("input", (e) => {
        strokeWidth = parseInt(e.target.value, 10);
        $("#stroke-value").textContent = strokeWidth;
    });

    $("#clear-canvas").addEventListener("click", () => {
        clearCanvas();
        resetResult();
    });

    // ===== Upload =====
    const dropzone = $("#dropzone");
    const fileInput = $("#file-input");
    const uploadPreview = $("#upload-preview");
    const uploadWrap = $("#upload-preview-wrap");
    let uploadedDataUrl = null;

    const handleFile = (file) => {
        if (!file) return;
        if (file.size > 5 * 1024 * 1024) {
            showError("File too large. Max 5 MB.");
            return;
        }
        const reader = new FileReader();
        reader.onload = (e) => {
            uploadedDataUrl = e.target.result;
            uploadPreview.src = uploadedDataUrl;
            uploadWrap.hidden = false;
        };
        reader.readAsDataURL(file);
    };

    fileInput.addEventListener("change", (e) => handleFile(e.target.files[0]));
    dropzone.addEventListener("dragover", (e) => { e.preventDefault(); dropzone.classList.add("dragover"); });
    dropzone.addEventListener("dragleave", () => dropzone.classList.remove("dragover"));
    dropzone.addEventListener("drop", (e) => {
        e.preventDefault();
        dropzone.classList.remove("dragover");
        handleFile(e.dataTransfer.files[0]);
    });

    $("#upload-clear").addEventListener("click", () => {
        uploadedDataUrl = null;
        fileInput.value = "";
        uploadWrap.hidden = true;
        resetResult();
    });

    // ===== Prediction =====
    const resultEmpty = $("#result-empty");
    const resultContent = $("#result-content");
    const resultLoading = $("#result-loading");
    const resultError = $("#result-error");

    const setView = (which) => {
        resultEmpty.hidden = which !== "empty";
        resultContent.hidden = which !== "content";
        resultLoading.hidden = which !== "loading";
        resultError.hidden = which !== "error";
    };

    const resetResult = () => setView("empty");

    const showError = (msg) => {
        $("#error-message").textContent = msg;
        setView("error");
    };

    const renderBarChart = (probs, predicted) => {
        const chart = $("#bar-chart");
        chart.innerHTML = "";
        probs.forEach((p, i) => {
            const col = document.createElement("div");
            col.className = "bar-col" + (i === predicted ? " active" : "");

            const pct = document.createElement("div");
            pct.className = "bar-pct";
            pct.textContent = p >= 0.01 ? `${(p * 100).toFixed(0)}%` : "";

            const track = document.createElement("div");
            track.className = "bar-track";
            const fill = document.createElement("div");
            fill.className = "bar-fill" + (i === predicted ? " top" : "");
            track.appendChild(fill);

            const label = document.createElement("div");
            label.className = "bar-label";
            label.textContent = i;

            col.append(pct, track, label);
            chart.appendChild(col);

            requestAnimationFrame(() => {
                fill.style.height = `${Math.max(p * 100, p > 0 ? 2 : 0)}%`;
            });
        });
    };

    const renderResult = (data) => {
        $("#big-digit").textContent = data.prediction;
        const confPct = (data.confidence * 100).toFixed(1);
        $("#confidence-text").textContent = `${confPct}%`;
        requestAnimationFrame(() => {
            $("#confidence-fill").style.width = `${confPct}%`;
        });

        const list = $("#top3-list");
        list.innerHTML = "";
        data.top3.forEach((item, idx) => {
            const li = document.createElement("li");
            li.innerHTML = `
                <span class="rank">${idx + 1}</span>
                <span class="digit">${item.digit}</span>
                <span class="conf">${(item.confidence * 100).toFixed(2)}%</span>
            `;
            list.appendChild(li);
        });

        $("#preview-img").src = data.preview;
        renderBarChart(data.probabilities, data.prediction);
        setView("content");
    };

    const predict = async (imageDataUrl, source) => {
        setView("loading");
        try {
            const res = await fetch("/api/predict", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ image: imageDataUrl, source }),
            });
            const data = await res.json();
            if (!res.ok) throw new Error(data.error || `HTTP ${res.status}`);
            renderResult(data);
        } catch (err) {
            showError(err.message || "Prediction failed.");
        }
    };

    const isCanvasBlank = () => {
        const data = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
        for (let i = 0; i < data.length; i += 4) {
            if (data[i] > 10 || data[i + 1] > 10 || data[i + 2] > 10) return false;
        }
        return true;
    };

    $("#predict-draw").addEventListener("click", () => {
        if (isCanvasBlank()) {
            showError("Canvas is empty. Draw a digit first.");
            return;
        }
        predict(canvas.toDataURL("image/png"), "canvas");
    });

    $("#predict-upload").addEventListener("click", () => {
        if (!uploadedDataUrl) {
            showError("Upload an image first.");
            return;
        }
        predict(uploadedDataUrl, "upload");
    });

})();
