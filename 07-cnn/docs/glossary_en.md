# Glossary — Convolutional Neural Networks (CNN)

| Term | Definition |
|------|-----------|
| **Convolutional layer** | Layer that applies learnable filters (kernels) to local patches of the input, sharing weights across spatial positions to detect features like edges and strokes. |
| **Kernel / Filter** | Small weight matrix (e.g. 3×3) slid over the input to produce a feature map. Each filter learns to detect a specific pattern. |
| **Feature map** | Output of a convolutional layer — a 2D grid of activations showing where a particular filter responded strongly. |
| **Padding** | Adding zeros around the input border (`same` padding) so the output feature map has the same spatial dimensions as the input. |
| **Stride** | Step size of the filter as it slides over the input. Stride > 1 reduces spatial dimensions. |
| **Pooling** | Downsampling operation that reduces spatial size. `MaxPooling` keeps the highest activation in each patch; reduces computation and adds translation invariance. |
| **Flatten** | Reshapes a 3D feature map (height × width × channels) into a 1D vector for the fully-connected classifier. |
| **Batch Normalization** | Normalizes activations across a mini-batch during training, accelerating convergence and reducing sensitivity to learning rate. |
| **Dropout** | Regularization technique: randomly zeros out a fraction of neurons during training to prevent co-adaptation and overfitting. |
| **Softmax** | Activation function in the output layer that converts raw scores (logits) to a probability distribution over classes. |
| **Sparse categorical cross-entropy** | Loss function for multi-class classification where labels are provided as integers (not one-hot vectors). |
| **Early Stopping** | Callback that halts training when a monitored metric (e.g. `val_loss`) stops improving, restoring the best weights seen. |
| **ReduceLROnPlateau** | Callback that reduces the learning rate by a factor when the monitored metric stagnates, helping escape local minima. |
| **Data Augmentation** | Applying random transforms (rotation, shift, zoom) to training images at run time to artificially increase dataset diversity. |
| **MNIST** | Modified National Institute of Standards and Technology dataset — 70 000 labelled 28×28 grayscale images of handwritten digits 0–9. |
| **Confusion matrix** | N×N table comparing true labels (rows) against predicted labels (columns); diagonal = correct predictions. |
| **ImageDataGenerator** | Keras utility that yields augmented mini-batches in real time without expanding the dataset on disk. |
| **Inference** | Running a trained model on new input to produce predictions, without any weight updates. |
| **Transfer learning** | Reusing weights from a model trained on one task (e.g. ImageNet) as a starting point for a related task. |
| **Receptive field** | Region of the original input that influences a particular neuron's activation; grows with network depth. |
