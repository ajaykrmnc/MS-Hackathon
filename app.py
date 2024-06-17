import os
import pickle
import streamlit as st
# import pymongo
from streamlit_option_menu import option_menu
from openai import AzureOpenAI


# Import custom module
from home import home
from bmi_calculator import bmi_calculator
from diabetes_prediction import diabetes_prediction
from heart_disease_prediction import heart_disease_prediction
from parkinsons_prediction import parkinsons_prediction
from chatbot import chatbot
from cancer_prediction import cancer_prediction
from datastore import table


# database setup
from pymongo import MongoClient
import streamlit as st


from pymongo.server_api import ServerApi
uri = st.secrets["uri"]

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
data = {
        'user_name': 'John Doe',
        'kind_of_disease': 'Flu',
        'level_of_disease': 3
}


# Set page configuration
st.set_page_config(page_title="AI Medical Health App",
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
                            'CureAI ChatBot', 'Admin Dashboard'],
                           menu_icon='microsoft',
                           icons=['house', 'robot', 'chat','database-fill-down'],
                           default_index=0)


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    if selected == 'Home':
        st.sidebar.write("Database connected sucessfully")
except Exception as e:
    print(e)

# Access the database
db = client['disease_database']

# Create a collection (similar to a table in relational databases)
collection = db['disease_collection']


    

if selected == 'Disease Checker':
    sub_selected = st.sidebar.selectbox('Select Disease',
                                ['BMI Calculator',
                                'Diabetes Prediction',
                                'Heart Disease Prediction',
                                'Breast Cancer',
                                'Parkinsons Prediction'])
    if sub_selected == 'BMI Calculator':
        bmi_calculator()
    elif sub_selected == 'Diabetes Prediction':
        diabetes_prediction(diabetes_model, collection)
    elif sub_selected == 'Heart Disease Prediction':
        heart_disease_prediction(heart_disease_model, collection)
    elif sub_selected == 'Parkinsons Prediction':
        parkinsons_prediction(parkinsons_model, collection)
    elif sub_selected == 'Breast Cancer':
        cancer_prediction(collection)
elif selected == 'CureAI ChatBot':
    chatbot()
elif selected == 'Home':
    home()
else:
    table(collection)

