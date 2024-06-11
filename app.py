import os
import pickle
import streamlit as st
import pymongo
from streamlit_option_menu import option_menu
from openai import AzureOpenAI


# Import custom modules
from bmi_calculator import bmi_calculator
from diabetes_prediction import diabetes_prediction
from heart_disease_prediction import heart_disease_prediction
from parkinsons_prediction import parkinsons_prediction
from chatbot import chatbot

ENDPOINT = "https://polite-ground-030dc3103.4.azurestaticapps.net/api/v1"
API_KEY = "445dcfab-cbf2-463c-a733-b66c7dd8ba50"
API_VERSION = "2024-02-01"
MODEL_NAME = "gpt-35-turbo"

client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)

#database
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["patient"]

# Create an array to store user name and result
patient_data = []

# Add user name and result to the array
patient_data.append({"name": "John Doe", "result": "Some result"})

# Save the patient data to the database
# mycol.insert_many(patient_data)




# Set page configuration
st.set_page_config(page_title="Disease Prediction and ChatBOt",
                   layout="wide",
                   page_icon="🧑‍⚕️")


# Load models
diabetes_model = pickle.load(open('./saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('./saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('./saved_models/parkinsons_model.sav', 'rb'))

#Sidebar for navigation
with st.sidebar:
    selected = option_menu('CureAI',
                           ['Home', 'Disease Checker',
                            'CureAI ChatBot'],
                           menu_icon='hospital-fill',
                           icons=['home', 'stethoscope', 'chat'],
                           default_index=0)

    

if selected == 'Disease Checker':
    sub_selected = st.sidebar.selectbox('Select Disease',
                                ['BMI Calculator',
                                'Diabetes Prediction',
                                'Heart Disease Prediction',
                                'Parkinsons Prediction'])
    if sub_selected == 'BMI Calculator':
        bmi_calculator()
    elif sub_selected == 'Diabetes Prediction':
        diabetes_prediction(diabetes_model)
    elif sub_selected == 'Heart Disease Prediction':
        heart_disease_prediction(heart_disease_model)
    elif sub_selected == 'Parkinsons Prediction':
        parkinsons_prediction(parkinsons_model)
elif selected == 'CureAI ChatBot':
    chatbot(client, MODEL_NAME)
else:
    st.title("welcome to our site")

