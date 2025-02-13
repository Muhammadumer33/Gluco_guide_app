import streamlit as st
import google.generativeai as genai

# App title and description
st.title("GlucoGuide: Smart Meal Planner")
st.write("A personalized meal planning app designed for diabetic patients. Enter your sugar levels and dietary preferences to receive customized meal suggestions for better glucose management.")

# Sidebar for user inputs
st.sidebar.header("Enter Your Details")
fasting_sugar = st.sidebar.number_input("Fasting Sugar Level (mg/dL)", min_value=50, max_value=400, value=100)
pre_meal_sugar = st.sidebar.number_input("Pre-Meal Sugar Level (mg/dL)", min_value=50, max_value=400, value=120)
post_meal_sugar = st.sidebar.number_input("Post-Meal Sugar Level (mg/dL)", min_value=50, max_value=400, value=150)
dietary_preference = st.sidebar.selectbox("Dietary Preference", ["Vegetarian", "Vegan", "Non-Vegetarian", "Keto", "Low-Carb", "Balanced Diet"])

# Function to call Claude's API
def get_meal_plan(sugar_levels, diet_preference):
    genai.configure(api_key=st.secrets["gemini_api_key"])
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(
        f"My fasting sugar is {sugar_levels['fasting']} mg/dL, and I prefer {diet_preference} meals. Suggest a healthy meal plan."
    )
    return response.text

# Display meal plan
if st.button("Generate Meal Plan"):
    sugar_levels = {
        "fasting": fasting_sugar,
        "pre_meal": pre_meal_sugar,
        "post_meal": post_meal_sugar
    }
    meal_plan = get_meal_plan(sugar_levels, dietary_preference)
    st.subheader("Your Personalized Meal Plan")
    st.write(meal_plan)
