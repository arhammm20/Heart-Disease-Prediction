# ❤️ Heart Disease Prediction System

## 📌 Overview

The Heart Disease Prediction System is a Machine Learning-based application that predicts the likelihood of heart disease in a patient based on medical attributes. The goal of this project is to assist in early detection and provide data-driven insights for better decision-making.


## 🚀 Features

* Predicts heart disease risk using a trained Machine Learning model
* Interactive web interface built with Streamlit
* Real-time user input processing
* Data preprocessing and feature scaling
* Fast and accurate predictions


## 🧠 Machine Learning Model

* Model: Logistic Regression
* Data Scaling: StandardScaler
* Libraries: Scikit-learn, Pandas, NumPy


## 📊 Input Features

The model takes the following inputs:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise-Induced Angina
* Oldpeak
* ST Slope


## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Joblib


## 📁 Project Structure

```
heart-disease-prediction/
│
├── app.py              # Streamlit application
├── model.pkl          # Trained model file
├── scaler.pkl         # Scaler object
├── columns.pkl        # Feature columns
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
streamlit run app.py
```


## 💻 Usage

1. Enter the required medical details in the input fields
2. Click on the **Predict** button
3. View the prediction result (risk of heart disease)


## 📈 Future Improvements

* Implement advanced models like Random Forest and XGBoost
* Improve UI/UX design
* Deploy on cloud platforms (AWS, Render, Streamlit Cloud)
* Add model explainability using SHAP or LIME


## ⚠️ Disclaimer

This project is for educational purposes only and should not be used as a substitute for professional medical advice.


## 🙌 Author

**Arham Farooqui**
