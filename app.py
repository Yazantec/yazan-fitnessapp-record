import streamlit as st

st.set_page_config(page_title="FitBalance", page_icon="🏋️")

st.title("🏋️ FitBalance")
st.write("Welcome to your fitness app!")

st.header("Your Information")

gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=100, value=18)
height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
weight = st.number_input("Weight (kg)", min_value=10, max_value=300, value=70)

if st.button("Calculate"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.success(f"Your BMI is: {bmi:.1f}")
