# CureAI - AI Medical Health App 

Welcome to the AI Medical Health App! This application is designed to assist users with various health-related predictions and calculations using machine learning. The app provides a user-friendly interface where you can enter your symptoms and select the service you need from the sidebar. Also you get help from AI powered chatbot for different health related queries 



## Members
- Ajay Kumar, IIT ISM Dhanbad
- Ankit Kumar Singh, IIT ISM Dhanbad

## Deployment
The AI Medical Health App is deployed and ready to use. You can access it through the following link: [CureAI on Streamlit](https://ms-hackathon.streamlit.app)

## Features
The AI Medical Health App offers the following services:

1. **Disease Prediction for common disease using Machine Learning**: 
    - Parkinson's disease
    - Diabetes
    - Heart disease
    - Breast cancer
    - BMI calculator
  For each disease, we have added a button to enter into the emergency queue, ensuring prompt attention for urgent cases.

1. **Chatbot Service**: Engage in a conversation with an AI-powered chatbot that can provide general health information, answer common medical questions, and offer guidance on various health topics.

2. **Emergency Patient Management**: Manage and prioritize patients in emergency situations based on the severity of their condition or other relevant factors.


## Home Page
When you open the app, you will be greeted with a welcome message and a list of available services. You can select the desired service from the sidebar. The home page also features an image of a doctor for a more engaging user experience.

<img src="assets/doctor.png" alt="Doctor" width="300" height="200">

## Installation
To get started with the AI Medical Health App, ensure you have Python 3.8 installed on your system. Follow the steps below to install Python 3.8 and the necessary dependencies.

### Step 1: Install Python 3.8
#### Windows
1. Download the Python 3.8 installer from the official [Python website](https://www.python.org/downloads/release/python-380/).
2. Run the installer and follow the on-screen instructions.
3. During installation, make sure to check the box that says "Add Python to PATH".

#### macOS
1. Download the Python 3.8 installer from the official [Python website](https://www.python.org/downloads/release/python-380/).
2. Open the downloaded package and follow the on-screen instructions to install Python 3.8.

#### Linux
Open a terminal and run the following commands:
```bash
sudo apt update
sudo apt install python3.8
```

### Step 2: Install Dependencies
1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

### Step 3: Add the api_key and MongoDB database uri
Add the MongoDB database and OpenAI API key to the `.streamlit/secrets.toml` file. Make sure to replace `YOUR_MONGODB_URI` with the URI of your MongoDB database and `YOUR_OPENAI_API_KEY` with your OpenAI API key.
```toml
[MongoDB]
uri = "YOUR_MONGODB_URI"

[OpenAI]
API_KEY = "YOUR_OPENAI_API_KEY"
```

### Step 4: Run the App
Start the Streamlit app by running the following command in the project directory:
```bash
streamlit run app.py
```
This will open the AI Medical Health App in your default web browser.

## Dependencies
Ensure that all dependencies listed in the `requirements.txt` file are installed. The `requirements.txt` file should include all the necessary packages to run the app.

Example `requirements.txt`:
```
pandas == 2.0.3
numpy == 1.24.4
scikit-learn == 1.0.2
streamlit == 1.35.0
streamlit-option_menu == 0.3.13
matplotlib-inline == 0.1.7
matplotlib == 3.7.5
openai == 1.34.0
pymongo == 4.7.3
plotly == 5.22.0
colorama == 0.4.6
seaborn == 0.13.2
scipy == 1.10.1
colorama == 0.4.6
```
## File structure
```
├── __pycache__
├── app.py
├── assets
│   └── doctor.png
├── home.py
├── bmi_calculator.py
├── cancer_prediction.py
├── chatbot.py
├── datastore.py // For the Dashboard
├── diabetes_prediction.py
├── heart_disease_prediction.py
├── model.pkl
├── parkinsons_prediction.py
├── readme.md
├── colab_files_to_train_models
│   ├── Multiple disease prediction system - Parkinsons.ipynb
│   ├── Multiple disease prediction system - diabetes.ipynb
│   └── Multiple disease prediction system - heart.ipynb
├── saved_models
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   ├── parkinsons_model.sav
│   └── scaler_heart.pkl
├── data.csv
├── dataset
│   ├── diabetes.csv
│   ├── heart.csv
│   └── parkinsons.csv
├── requirements.txt
├── scaler.pkl
└── style.css
```


## Usage

Once the app is running, you can use the sidebar to select the service you want to use. Enter your symptoms or relevant data as prompted by the app, and receive predictions or calculations based on the service selected.

We hope this app helps you with your health-related inquiries and provides useful predictions to assist in your medical needs. If you have any questions or need further assistance, feel free to contact us.


## Admin Dashboard
In addition to the existing features, we have implemented an Admin Dashboard specifically designed for hospital management. This dashboard allows hospital staff to create and manage queues for patients based on the predicted values obtained from their test reports.

### Key Features
- **Queue Creation**: Hospital staff can create separate queues for different diseases based on the predicted values obtained from the patients' test reports.
- **Priority Management**: The Admin Dashboard allows staff to prioritize patients in the queues based on the severity of their condition or other relevant factors.
- **Queue Monitoring**: Hospital staff can monitor the status of each queue, including the number of patients waiting and any urgent cases that require immediate attention.

With the Admin Dashboard, hospital management can efficiently organize patient queues and ensure timely and appropriate medical attention based on the predicted values obtained from the patients' test reports.

Please note that the Admin Dashboard is intended for hospital management use only and requires appropriate access credentials.

We are continuously working on enhancing the AI Medical Health App to provide the best possible user experience and meet the needs of both patients and healthcare professionals.

## Different Models Used
### 1. BMI-Calculator
File Location -> bmi_calculator.py<br>

Body Mass Index (BMI) is a simple and widely used method for assessing an individual's body weight relative to their height. It is calculated by dividing a person's weight in kilograms by the square of their height in meters (kg/m²). Here are some reasons why BMI is useful:
The BMI categories used in this application are:
- Underweight: BMI < 18.5
- Normal weight: 18.5 <= BMI < 24.9
- Overweight: 25 <= BMI < 29.9
- Obese: BMI >= 30

### 2. Diabetes Predictor 
```
File Location -> colab_files_to_train_models -> Multiple disease prediction system - diabetes.ipynb<br>
Dataset Location -> dataset -> diabetes.csv
```

The algorithm being developed for this research uses machine learning to forecast an individual's risk of developing diabetes based on a number of different health indicators. Using Streamlit as the UI framework, the application lets users enter pertinent health information and get estimates of their risk of developing diabetes<br>
Features<br>
- Input health parameters including glucose levels, blood pressure, skin thickness, insulin levels, BMI, age, etc.
- Predict the likelihood of diabetes based on the input parameters.
- User-friendly interface built with Streamlit.
- Visualize the results and health data easily.

This Model is build over Support Vector Classifier, A Machine Learning Model and Provides a accuracy of 77% over the test data

### 3. Heart Disease Predictor
```
File Location -> colab_files_to_train_models -> Multiple disease prediction - heart.ipynb<br>
Dataset Location -> dataset -> heart.csv
```

This project is a machine learning-based system that uses a variety of health metrics to estimate an individual's risk of heart disease. Using Streamlit as the UI framework, the application lets users enter pertinent health information and get risk estimates for heart disease.<br>
Features<br>
- Input health parameters including age, sex, blood pressure, cholesterol levels, and more.
- Predict the likelihood of heart disease based on the input parameters.
- User-friendly interface built with Streamlit.
- Visualize the results and health data easily.
- Proper Exploratory Data Analysis has been done to find about important attributes.<br>

Following machine learning models has been tested<br>
- KNN + tune hyperparameters
- SVM + tune hyperparameters
- Decision Trees + tune hyperparameters
- Random Forest + tune hyperparameters

Finally support vector classifier has been selected with a maximum accuracy of 93%<br>

### 4. Parkinsons Disease Predictor
```
File Location -> colab_files_to_train_models -> Multiple disease prediction - Parkinsons.ipynb<br>
Dataset Location -> dataset -> parkinsons.csv
```

With the use of several health indicators, this project's machine learning-based system will be able to forecast a person's risk of developing Parkinson's disease. Using Streamlit as the UI framework, the program lets users enter pertinent health information and get estimates of their chance of developing Parkinson's disease.<br>
Features<br>
- input health parameters including voice measurements and other relevant medical data.
- Proper Exploratory Data Analysis has been done to find the similarity between various types of attributes also the the impact of each feature on the probability of the positive class.
- Predict the likelihood of Parkinson's disease based on the input parameters.
- User-friendly interface built with Streamlit.
- Visualize the results and health data easily.

Following Machine Learning Models has been used to determine the outcome for Disease
- k-Nearest Neighbors (k-NN)
- GridSearchCV
- Logistic Regression
- Support Vector Machines (SVM)
- Random Forest Model

Final Model used to for classification is Random Forest Classifier with accuracy of 89%

### 5. Breast Cancer Classifier (Malignant/Benign)
```
File Location -> cancer_prediction.py
Dataset Location -> data.csv
```

Having various Health indicators as attributes like a cell's mean radius, Texture Mean, perimeter Mean, Area mean, etc this Machine Learning Model predicts whether the breast cancer is of malignant or benign type.<br>
Features<br>
- input health parameters including cell's Texture and other relevant data from Data.csv file
- Exploratory Data Analysis has been done.
- Standarization of data also has been done to improve the model's accuracy.
- User-friendly interface built with Streamlit.
- Visualization of result with best accuracy of whether the person is suffering from malignant or benign tumour.

Machine Learning Model used -> Logistic Regression<br>
Accuracy of model -> 97%


Enjoy using the AI Medical Health App!
