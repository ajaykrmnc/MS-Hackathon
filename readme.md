# CureAI - AI Medical Health App 

Welcome to the AI Medical Health App! This application is designed to assist users with various health-related predictions and calculations using artificial intelligence. The app provides a user-friendly interface where you can enter your symptoms and select the service you need from the sidebar.

## Features

The AI Medical Health App offers the following services:

1. **BMI Calculator**
2. **Parkinson's Disease Prediction**
3. **Diabetes Prediction**
4. **Heart Disease Prediction**
5. **Breast Cancer Prediction**
6. **Chatbot**

## Home Page

When you open the app, you will be greeted with a welcome message and a list of available services. You can select the desired service from the sidebar. The home page also features an image of a doctor for a more engaging user experience.

![Doctor](assets/doctor.png)

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

### Step 3: Run the App

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

## Usage

Once the app is running, you can use the sidebar to select the service you want to use. Enter your symptoms or relevant data as prompted by the app, and receive predictions or calculations based on the service selected.

We hope this app helps you with your health-related inquiries and provides useful predictions to assist in your medical needs. If you have any questions or need further assistance, feel free to contact us.

Enjoy using the AI Medical Health App!