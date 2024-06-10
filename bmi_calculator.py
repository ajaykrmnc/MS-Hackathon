import streamlit as st

def bmi_calculator():
    st.title('Calculate your BMI Index')
    st.write('Body mass index (BMI) is a value derived from the mass and height of a person. The BMI is defined as the body mass divided by the square of the body height, and is expressed in units of kg/m², resulting from mass in kilograms and height in metres.')

    st.write("**Let's check your BMI ↓**")
    weight = st.number_input("Enter your weight (in kg)")
    height = st.number_input("Enter your height (in meter)")

    if st.button('Calculate BMI'):
        bmi = weight / (height ** 2)
        st.text(f"Your BMI index is {bmi}.")

        if bmi < 16:
            st.error("You are Extremely Underweight")
            st.toast('Add extra calories to your meals and doing some exercise to increase your appetite!', icon='🥙')
        elif 16 <= bmi < 18.5:
            st.warning("You are Underweight")
            st.toast('Eat more high-protein meats on your food!', icon='🥩')
        elif 18.5 <= bmi < 25:
            st.success("You are Healthy")
            st.balloons()
        elif 25 <= bmi < 30:
            st.warning("You are Overweight")
            st.toast('Eat more healthy food!', icon='🍎')
        elif bmi >= 30:
            st.error("You are Extremely Overweight")
            st.toast('Eat a balanced and do some diet!', icon='💪')
