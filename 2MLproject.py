import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("calories_burned_prediction_model.pkl")


st.set_page_config(
    page_title="Calories Burned Prediction",
    page_icon="🏋️",
    layout="centered"
)


st.title("🏋️ Calories Burned Prediction")

st.write(
    "Enter the workout and personal details below "
    "to predict calories burned."
)


# ============================================================
# USER INPUTS
# ============================================================

age = st.number_input(
    "Age",
    min_value=10,
    max_value=100,
    value=25
)


gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)


weight = st.number_input(
    "Weight (kg)",
    min_value=20.0,
    max_value=200.0,
    value=70.0
)


height = st.number_input(
    "Height (m)",
    min_value=1.0,
    max_value=2.5,
    value=1.70
)


session_duration = st.number_input(
    "Session Duration (hours)",
    min_value=0.1,
    max_value=10.0,
    value=1.0
)


workout_type = st.selectbox(
    "Workout Type",
    [
        "Cardio",
        "HIIT",
        "Strength",
        "Yoga"
    ]
)


water_intake = st.number_input(
    "Water Intake (liters)",
    min_value=0.0,
    max_value=10.0,
    value=2.0
)


workout_frequency = st.number_input(
    "Workout Frequency (days/week)",
    min_value=0,
    max_value=7,
    value=3
)


experience_level = st.number_input(
    "Experience Level",
    min_value=1,
    max_value=5,
    value=2
)


# ============================================================
# ADDITIONAL FEATURES REQUIRED BY YOUR MODEL
# ============================================================

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=23.0
)


fat_percentage = st.number_input(
    "Fat Percentage",
    min_value=1.0,
    max_value=60.0,
    value=20.0
)


resting_bpm = st.number_input(
    "Resting BPM",
    min_value=30,
    max_value=120,
    value=70
)


avg_bpm = st.number_input(
    "Average BPM",
    min_value=40,
    max_value=220,
    value=120
)


max_bpm = st.number_input(
    "Maximum BPM",
    min_value=50,
    max_value=250,
    value=180
)


# ============================================================
# PREDICTION
# ============================================================

if st.button("🔥 Predict Calories Burned"):

    input_data = pd.DataFrame({
        
        "Age": [age],

        "Gender": [gender],

        "Weight (kg)": [weight],

        "Height (m)": [height],

        "Session_Duration (hours)": [
            session_duration
        ],

        "Workout_Type": [workout_type],

        "Water_Intake (liters)": [
            water_intake
        ],

        "Workout_Frequency (days/week)": [
            workout_frequency
        ],

        "Experience_Level": [
            experience_level
        ],

        "BMI": [bmi],

        "Fat_Percentage": [
            fat_percentage
        ],

        "Resting_BPM": [
            resting_bpm
        ],

        "Avg_BPM": [
            avg_bpm
        ],

        "Max_BPM": [
            max_bpm
        ]
    })


    try:

        prediction = model.predict(
            input_data
        )

        st.success(
            f"🔥 Predicted Calories Burned: "
            f"{prediction[0]:.2f} calories"
        )

    except Exception as e:

        st.error(
            "Prediction failed."
        )

        st.exception(e)
