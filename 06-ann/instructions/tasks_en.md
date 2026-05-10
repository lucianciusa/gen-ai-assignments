### **Case Study: Neural Network Model for Housing Price Prediction**
---

## **1. Business Case Discovery**  
### **1.1 Business Context**  
You are part of an analysis team at a real estate investment firm. The company seeks to improve the accuracy of property valuation aiming to maximize profitability and minimize risks. In this market, errors in price estimation can result in millionaire losses.

The company has a historical dataset
https://www.kaggle.com/datasets/yasserh/housing-prices-dataset
with the following variables: 

- **Input features:**  
  - `area`: Total area of the house in square feet.  
  - `bedrooms`: Number of bedrooms.  
  - `bathrooms`: Number of bathrooms.  
  - `stories`: Number of stories.  
  - `mainroad`: Whether the house is on a main road (Yes/No).  
  - `guestroom`: Whether it has a guest room (Yes/No).  
  - `basement`: Whether it has a basement (Yes/No).  
  - `hotwaterheating`: Whether it has hot water heating (Yes/No).  
  - `airconditioning`: Whether it has air conditioning (Yes/No).  
  - `parking`: Number of parking spaces.  
  - `prefarea`: Whether it is in a preferential area (Yes/No).  
  - `furnishingstatus`: Furnishing status (Furnished, Semi-Furnished, Unfurnished).  
- **Target variable:**  
  - `price`: Sale price of the property (continuous variable to predict).  

### **1.2 Project Objective**  
Develop a neural network model to predict housing prices with a higher accuracy than traditional methods like linear regression.

### **1.3 Stakeholders and Requirements**  
- **Investors:** Looking for predictions with a margin of error lower than 15%.
- **Legal Team:** Require the model to be interpretable to justify decisions in audits.
- **Technical Team:** The implementation must be scalable and compatible with cloud environments (AWS/GCP), using Docker Containers.

### **1.4 Success Metrics**  
- **Root Mean Square Error (RMSE):** Lower than 15% of the average housing price.  
- **Coefficient of determination (R²):** Greater than 0.60.  

### **1.5 Anticipated Challenges**  
- **Multicollinearity:** Variables like `area`, `bedrooms` and `bathrooms` might be correlated.
- **Skewed distributions:** Binary and categorical variables might need proper encoding.
- **Overfitting:** The neural network might memorize data instead of generalizing.

---

## **2. Data Processing**  
### **2.1 Initial Loading and Exploration**  
The student must load the dataset, visualize the first rows, and explore the data distribution with histograms and box plots. The use of `pandas` and `matplotlib` is recommended.

**Hints:**
- Identify distributions with long tails and outliers.
- Check for the presence of null values.

### **2.2 Correlation Analysis**  
The student will generate a correlation matrix to analyze relationships between variables. The use of `seaborn` is suggested.

**Hints:**
- Evaluate which variables have a high correlation with `price`.
- Consider removing redundant variables.

### **2.3 Data Preprocessing**  
- **Handling missing values:** If any, impute them with the median or mode according to the variable type.
- **Encoding categorical variables:** Convert `mainroad`, `guestroom`, `basement`, etc., into numerical values.
- **Normalization:** Scale numerical variables using `StandardScaler` or `MinMaxScaler`. 

### **2.4 Train-Test Split**  
The student must divide the data into training and testing (80/20). It is recommended to use `train_test_split` from `sklearn`.

---

## **3. Model Planning**  
### **3.1 Problem Definition**  
- **Model Type:** Regression with neural network.
- **Input:** 12 preprocessed features.
- **Output:** Price prediction.

### **3.2 Network Architecture**  
The student must design a neural network with:
- **Input Layer:** 12 neurons (one per feature).
- **Hidden Layers:** Two dense layers with ReLU activation.
- **Output Layer:** 1 neuron with linear activation.

### **3.3 Loss Function and Optimizer**  
- **Loss Function:** Mean Squared Error (MSE).
- **Optimizers to compare:** Adam and SGD with momentum.

### **3.4 Model Evaluation**  
Metrics such as MAE, RMSE, and R² will be analyzed, and cross-validation will be used (K-Fold with k=5).

---

## **4. Model Building and Selection**  
### **4.1 Implementation in Keras**  
The student will build the model using `keras.Sequential()`.

### **4.2 Model Training**  
Train the network with an adequate number of epochs and an optimal batch size, ensuring effective validation to avoid overfitting.

Example: 100 epochs with `batch_size=32` and 20% validation.

### **4.3 Hyperparameter Experimentation**  
- Test different learning rates (`0.001`, `0.0001`).
- Compare `batch_size=16` vs `64`.
- Apply regularization with `Dropout` or `L2`.

### **4.4 Evaluation on Test Set**  
The student will compare the final metrics with those of the training set to verify if there is overfitting.

---

## **5. Presentation of Results**  

### **5.1 Prediction Evaluation**  
The student must analyze the quality of the predictions using scatter plots, trend lines, and key metrics like RMSE and R². It is recommended to visually interpret how predictions align with actual values and detect possible error patterns.  

### **5.2 Error Analysis**  
Predictions with significant errors will be identified, especially those with deviations greater than 10% of the real price. The student must investigate if these errors are due to outliers, lack of representativeness in the training data, or model limitations.  

### **5.3 Comparison with Baseline (OPTIONAL)**  
To evaluate the effectiveness of the model, its results will be compared with a traditional linear regression model. Differences in RMSE, R², and error distribution will be analyzed to justify the use of a neural network over simpler methods.

---

## **6. Deployment**  
### **6.1 Model Serialization**  
The model will be saved in `.h5` or `.keras` format for specific reuse.

### **6.2 Creation of Prediction API (OPTIONAL due to time constraints)**  
The student must implement an endpoint with `Flask` that receives data and returns a prediction.

---

### **Conclusion**  
This case study allows applying key concepts of the deep learning model lifecycle, combining theory and practice. The student is expected to document each decision made in a technical report.