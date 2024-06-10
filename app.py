import os
import pickle
import streamlit as st
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

# Set page configuration
st.set_page_config(page_title="Disease Prediction and ChatBOt",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Checker and AI Chatbot',
                           ['BMI Calculator',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'CureAI ChatBot'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person', '', 'bot'],
                           default_index=0)

# Load models
diabetes_model = pickle.load(open('./saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('./saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('./saved_models/parkinsons_model.sav', 'rb'))

# Route to the appropriate module
if selected == 'BMI Calculator':
    bmi_calculator()
elif selected == 'Diabetes Prediction':
    diabetes_prediction(diabetes_model)
elif selected == 'Heart Disease Prediction':
    heart_disease_prediction(heart_disease_model)
elif selected == 'Parkinsons Prediction':
    parkinsons_prediction(parkinsons_model)
elif selected == 'CureAI ChatBot':
    chatbot(client, MODEL_NAME)
