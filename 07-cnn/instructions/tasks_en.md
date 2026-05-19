### **Case Study: Convolutional Neural Network Model for Digit Recognition**
---

## **1. Business Case Discovery**

### **1.1 Business Context and Background**
A major shipping company has decided to modernize its mail, package, and parcel routing system. Currently, the sorting process is semi-automatic and requires manual intervention, causing delays and delivery errors.
The business has identified that automatic recognition of the digits that make up the postal code on packages can streamline the process and reduce operational costs, improving customer satisfaction.

### **1.2 Project Objective**
The purpose is to develop a digit recognition system based on a convolutional neural network model that will:
- Correctly identify postal code digits on package images.
- Automate routing and sorting based on the postal code.

### **1.4 Success Metrics**
- **Accuracy:** Percentage of digits correctly recognized in each image.
- **Inference Time:** Time required to process each image, key for real-time applications.
- **Number of Parameters:** Comparison of model efficiency, evaluating complexity and generalization capacity.

### **1.5 Challenges and Considerations**
- **Image Quality and Variability:** Different lighting conditions, angles, and noise can make classification difficult.
- **Overfitting and Underfitting:** Balancing model complexity so it does not over-adapt to the training samples.

---

## **2. Data Processing**

### **2.1 Training Dataset**
For this case study, we will use the **MNIST** (Modified National Institute of Standards and Technology) dataset, which contains **70,000 grayscale images (28x28 pixels) of handwritten digits (0-9)**. This dataset is widely used for image classification tasks and will serve as the basis for training our digit recognition model for postal codes.

Students can access this dataset through libraries like **TensorFlow/Keras (`tf.keras.datasets.mnist`)** or download it from platforms like **Kaggle**.

### **2.2 Exploratory Data Analysis and Visualization**
To understand the nature of the data, the student must:

- Visualize multiple samples of digits in different formats.
    - Group images by class and observe if some digits are represented more frequently than others.

- Use histograms and scatter plots to analyze the class distribution.
    - Use histograms to see how many images there are of each number (0-9).
    - Are there classes with more images than others? If so, this could affect model training.
    - If there is an imbalance, consider techniques like oversampling or targeted augmentation.

- Detect possible anomalies or biases in the image distribution.
    - Look for mislabeled or low-quality images (blurry, noisy, or poorly written digits).
    - Common errors:
        Corrupted images (random pixels).
        Poorly centered or rotated digits.
        Incorrect labels (e.g., a "5" labeled as a "6").
    - Think of strategies to handle these data: Should they be removed or corrected?

### **2.3 Image Cleaning and Preprocessing**

The **MNIST** dataset is largely preprocessed, but it is important to ensure the data is in the proper format before training the neural network.

- **Resizing and Normalization:** It is not necessary to resize the images, as they all have a uniform resolution of **28x28 pixels**. However, pixel values are in the range **[0, 255]**, so they must be normalized by dividing by **255** to scale them to the **[0,1]** range, which helps stabilize model training.

- **Data Augmentation:** Although MNIST is a well-balanced dataset, adding **data augmentation** can improve model generalization. It is recommended to apply transformations such as **rotations, translations, zoom, and brightness changes** to simulate variations in digit writing and make the model more robust.

- **Format Conversion:** The images are in grayscale and are stored as NumPy arrays. For them to be processed correctly by a CNN in Keras/TensorFlow, it is necessary to ensure they have the proper shape **(n_samples, 28, 28, 1)**, adding a channel dimension (`reshape(-1, 28, 28, 1)`) if necessary.

### **2.4 Data Splitting: Train, Validation, and Test**
- Split the dataset into three sets: training (70%), validation (15%), and testing (15%).
- Ensure that each set maintains the same class distribution to avoid biases in evaluation.

---

## **3. Model Planning**

### **3.1 Problem Definition and Approach**
- **Problem Type:** Image classification, where each image represents a digit from 0 to 9.
- **Objective:** Achieve high accuracy in digit identification, minimizing errors that could affect package routing.

### **3.2 Proposed Work**
The objective is to build a functional CNN for digit classification and have it ready to be evaluated with the MNIST dataset.

### **3.3 Training Criteria**
- Correctly prepare the data so it has the proper shape for a CNN.
- Train the model with a clear train/validation/test flow.
- Monitor metrics during training to detect overfitting or underfitting.

### **3.4 Loss Function and Evaluation**
- **Loss Function:** Use categorical cross-entropy (`categorical_crossentropy`) or its equivalent variant depending on label encoding.
- **Evaluation:** Measure accuracy and loss, and analyze the confusion matrix and error examples.

---

## **4. Model Building and Selection**

### **4.1 Construction and Training**
The student must implement the CNN and train it on MNIST, taking care of preprocessing, validation, and learning stability.

### **4.2 Validation and Analysis**
- **Number of Epochs and Batch Size:** Start with moderate values and observe the evolution of loss and accuracy.
- **Metric Monitoring:** Review behavior in training and validation.
- **Early Stopping:** Use it if training begins to degrade validation.

### **4.3 Final Model Selection**
Select the configuration that generalizes best and document why it was chosen.

---

## **5. Presentation of Results**

### **5.1 Quantitative Analysis of Metrics**
The student must present the results obtained based on:
- **Accuracy:** Percentage of correctly classified digits.
- **Loss and Cross-Entropy:** Evolution during training and validation.
- **Model Behavior:** Results on train, validation, and test.

### **5.2 Result Visualization**
- **Training and Validation Curves:** Plot the evolution of loss and accuracy over epochs to detect overfitting or inadequate convergence.
- **Confusion Matrix:** Visualize the distribution of correct predictions and errors among the 10 classes to identify digits that might be confused.
- **Error Analysis:** Show examples of misclassified images and investigate possible causes (image quality, ambiguity, etc.).

### **5.3 Comparison and Critical Reflection**
- Discuss whether the model generalizes well or shows overfitting.
- Analyze the balance between accuracy, robustness, and inference cost.
- Propose possible future improvements in a reasoned manner.

---

## **6. Deployment**

### **6.1 Model Serialization and Storage**
- **Model Saving:** The student must save the final model in an appropriate format (e.g., `.h5` or `.keras`) to facilitate its reuse.

### **6.2 Development of an API for Inference**
- **Web Service Implementation:** Create an endpoint (e.g., using Flask or FastAPI) that receives package images and returns the digit prediction.
- **Simple Interface:** Propose a simple frontend to upload images and display the prediction, for example with **Streamlit** or a similar alternative. Here you can be creative and invent possible use cases and useful applications.
- **Production Optimization:** Ensure the service runs efficiently and is easy to deploy.

### **6.3 Testing and Validation in Real Environment**
- **Integration Testing:** Perform tests with real package images to evaluate the model's robustness in operational conditions.

---

### **Conclusion**
The problem of recognizing digits in postal codes not only reinforces knowledge of convolutional neural networks but also invites exploration of the importance of experimentation, validation, and system integration in a productive workflow. Each student is expected to justify their choices, document their process, and propose improvements based on their experimental findings.