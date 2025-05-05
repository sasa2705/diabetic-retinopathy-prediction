# Diabetic Retinopathy Prediction System

A comprehensive web application for predicting diabetic retinopathy risk using machine learning. The system combines Django for the backend and Streamlit for the prediction interface.

## Features
- **User Authentication**: Secure login and registration system
- **Risk Assessment**: Predicts diabetic retinopathy risk based on:
  - Age
  - Systolic Blood Pressure (Normal range: < 120 mmHg)
  - Diastolic Blood Pressure (Normal range: < 80 mmHg)
  - Cholesterol Levels (Normal range: 125-200 mg/dl)
- **Dashboard**: Visual representation of prediction results
- **PDF Reports**: Generate detailed PDF reports of predictions

## Project Structure
```
.
├── app.py                 # Streamlit prediction interface
├── dr_home.py            # Django home view
├── model.py              # Machine learning model training and preprocessing
├── model.joblib          # Trained model file
├── scaler.joblib         # Feature scaler
├── prediction/           # Django prediction app
├── retinopathy_prediction/  # Django project settings
├── static/               # Static files (CSS, JS, images)
├── templates/            # HTML templates
├── media/                # User-uploaded files
└── requirements.txt      # Project dependencies
```

## Technical Stack
- **Backend**: Django 5.0.2
- **Frontend**: HTML, CSS, Bootstrap 5
- **Machine Learning**: scikit-learn, pandas, numpy
- **Data Visualization**: matplotlib, seaborn
- **PDF Generation**: reportlab
- **Image Processing**: Pillow

## Setup Instructions

1. **Clone the repository**
```bash
git clone <repository-url>
cd <project-directory>
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Start the development server**
```bash
# Start Django server
python manage.py runserver

# In a separate terminal, start Streamlit
streamlit run app.py
```

## Data Description
- **Dataset**: `pronostico_dataset (1).csv`
- **Size**: 6,002 records
- **Target Variable**: 
  - 0: No Retinopathy
  - 1: Retinopathy
- **Features**:
  - Age: Patient's age in years
  - Systolic BP: Blood pressure measurement (mmHg)
  - Diastolic BP: Blood pressure measurement (mmHg)
  - Cholesterol: Blood cholesterol level (mg/dl)

## Model Performance
The system uses a trained machine learning model with the following characteristics:
- **Model Type**: Classification model
- **Storage**: Saved as `model.joblib`
- **Feature Scaling**: StandardScaler saved as `scaler.joblib`

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
[Specify your license here]

## Contact
[Add contact information] 