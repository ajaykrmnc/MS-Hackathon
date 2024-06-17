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
api_key = "YOUR_OPENAI_API_KEY"
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

Enjoy using the AI Medical Health App!
