# Diabetic Retinopathy Prediction System

A Streamlit web application that uses machine learning to predict the risk of diabetic retinopathy based on patient health parameters.

## About

Diabetic retinopathy is a diabetes complication that affects the eyes. It's caused by damage to the blood vessels in the tissue at the back of the eye (retina). Early detection can help prevent vision loss.

This application uses a Random Forest Classifier trained on patient health data to predict the risk of diabetic retinopathy.

## Features

- Predict diabetic retinopathy risk based on patient health parameters
- Generate and download PDF reports
- Visualize health parameters and their status
- View feature importance in prediction
- Access information about diabetic retinopathy and prevention measures

## Requirements

- Python 3.8+
- Required Python packages listed in `requirements.txt`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/diabetic-retinopathy-prediction.git
   cd diabetic-retinopathy-prediction
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the model training script (if model.joblib and scaler.joblib don't exist):
   ```bash
   python model.py
   ```

4. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Deployment on Streamlit Cloud

This application can be deployed on Streamlit Cloud by following these steps:

1. Push your repository to GitHub
2. Sign up for Streamlit Cloud at https://streamlit.io/cloud
3. Create a new app and connect it to your GitHub repository
4. Configure the app with the following settings:
   - Main file path: `app.py`
   - Python version: 3.8+

## Project Structure

- `app.py`: Main Streamlit application
- `model.py`: Model training script
- `model.joblib`: Trained Random Forest model
- `scaler.joblib`: Standard scaler for data preprocessing
- `requirements.txt`: Required Python packages
- `.streamlit/`: Streamlit configuration

## Data

The model is trained on patient health data with the following features:
- Age
- Systolic Blood Pressure
- Diastolic Blood Pressure
- Cholesterol

## Model Performance

- Accuracy: ~85-90%
- Sensitivity: ~80-85%
- Specificity: ~85-90%

## Limitations

This model is intended as a screening tool and should not replace professional medical diagnosis. Always consult with a healthcare professional for proper diagnosis and treatment.

## License

MIT 