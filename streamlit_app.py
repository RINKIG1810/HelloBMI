import streamlit as st

def calculate_bmi(weight_kg, height_ft):
    # Convert height from feet to meters (1 foot = 0.3048 meters)
    height_m = height_ft * 0.3048
    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    return bmi

def get_bmi_category(bmi):
    # Determine the category based on BMI value
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Streamlit UI
st.title("BMI Calculator")

# Input fields for weight and height
weight_kg = st.number_input("Enter your weight (in kg):", min_value=0.0, format="%.2f")
height_ft = st.number_input("Enter your height (in feet):", min_value=0.0, format="%.2f")

if st.button("Calculate BMI"):
    if weight_kg > 0 and height_ft > 0:
        # Calculate BMI
        bmi = calculate_bmi(weight_kg, height_ft)
        category = get_bmi_category(bmi)
        
        # Display the result
        st.write(f"Your BMI: {bmi:.2f}")
        st.write(f"BMI Category: {category}")
    else:
        st.write("Please enter valid weight and height.")

