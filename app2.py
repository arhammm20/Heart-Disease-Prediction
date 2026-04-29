import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(page_title="Heart Risk Predictor", page_icon="❤️", layout="wide")

# Load model
model = joblib.load("LR_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

# Title
st.markdown("<h1 style='text-align: center; color: red;'>❤️ Heart Disease Risk Predictor</h1>", unsafe_allow_html=True)
st.markdown("---")

# Layout
col1, col2 = st.columns(2)

# Left column (Basic Info)
with col1:
    st.subheader("👤 Patient Information")
    age = st.slider("Age", 18, 100, 40)
    sex = st.selectbox("Sex", ["M", "F"])
    max_hr = st.slider("Max Heart Rate", 60, 220, 150)
    exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])

# Right column (Medical Info)
with col2:
    st.subheader("🩺 Medical Details")
    chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
    oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

st.markdown("---")

# Predict button
if st.button("🔍 Predict Risk", use_container_width=True):

    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])
    input_df = pd.get_dummies(input_df)

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]
    probability = model.predict_proba(scaled_input)[0][1]

    st.markdown("## 📊 Result")

    # Progress bar for risk
    st.progress(int(probability * 100))

    st.write(f"### 🔢 Risk Score: **{probability*100:.2f}%**")

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")

        st.markdown("""
        ### 🧠 Recommendations:
        - Reduce cholesterol intake
        - Regular exercise (30 min/day)
        - Avoid smoking & alcohol
        - Monitor BP regularly
        """)

    else:
        st.success("✅ Low Risk of Heart Disease")

        st.markdown("""
        ### 💚 Keep it up:
        - Maintain healthy diet
        - Stay active
        - Regular checkups
        """)
