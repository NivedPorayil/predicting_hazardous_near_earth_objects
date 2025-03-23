import streamlit as st
import pickle
import numpy as np
import sklearn

with open("neo_risk_prediction.pkl", "rb") as file:
    model = pickle.load(file)

bg_image_url = "https://bgr.com/wp-content/uploads/2021/11/comet-earth.jpg?quality=82&strip=all"


st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("{bg_image_url}") no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌠 Near-Earth Object Hazard Predictor")
st.markdown("### Please Enter the Following Details : ")

est_diameter_min = st.number_input("Estimated Diameter Min (km)", min_value=0.0, step=0.01, format="%.6f")
est_diameter_max = st.number_input("Estimated Diameter Max (km)", min_value=0.0, step=0.01, format="%.6f")
relative_velocity = st.number_input("Relative Velocity (km/s)", min_value=0.0, step=0.01, format="%.6f")
miss_distance = st.number_input("Miss Distance (km)", min_value=0.0, step=0.01, format="%.6f")
absolute_magnitude = st.number_input("Absolute Magnitude", min_value=0.0, step=0.01, format="%.6f")

if st.button("Predict"):
    input_features = np.array(
        [[est_diameter_min, est_diameter_max, relative_velocity, miss_distance, absolute_magnitude]])
    prediction = model.predict(input_features)

    if prediction[0]:
        st.error("⚠️ This Object Could Be **Potentially Hazardous**!")
    else:
        st.success("✅ This Object is Likely To Be **Not Hazardous**.")
