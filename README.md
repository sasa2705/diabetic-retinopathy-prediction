# Diabetic Retinopathy Prediction System

This project aims to predict whether a patient will develop diabetic retinopathy based on various health parameters.

## Features
- Age
- Systolic Blood Pressure
- Diastolic Blood Pressure
- Cholesterol Levels

## Project Structure
- `app.py`: Main Streamlit application
- `model.py`: Model training and preprocessing
- `requirements.txt`: Project dependencies
- `pronostico_dataset (1).csv`: Dataset

## Setup Instructions
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run app.py
```

## Data Description
- Target Variable: Prognosis (0: No Retinopathy, 1: Retinopathy)
- Features:
  - Age: Patient's age
  - Systolic BP: Normal range < 120mmHg
  - Diastolic BP: Normal range < 80mmHg
  - Cholesterol: Normal range 125-200 mg/dl

## Model Performance
The model is trained using various machine learning algorithms and evaluated based on accuracy, precision, recall, and F1-score. 