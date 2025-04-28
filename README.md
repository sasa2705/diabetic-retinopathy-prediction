# Diabetic Retinopathy Prediction System

This web application predicts whether a patient will develop diabetic retinopathy based on various health parameters.

## Features
- Patient registration and management
- Health record tracking
- Diabetic retinopathy risk prediction
- PDF report generation
- Account management

## Technologies Used
- Django web framework
- Bootstrap for styling
- Crispy Forms for form rendering
- ReportLab for PDF generation
- Machine learning model for prediction

## Project Structure
- `prediction/`: Django app containing the core functionality
- `retinopathy_prediction/`: Django project settings
- `templates/`: HTML templates
- `static/`: Static assets (CSS, JS, images)
- `media/`: Uploaded files and generated PDFs
- `manage.py`: Django command-line utility

## Local Development Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

5. Visit http://localhost:8000 in your browser

## Netlify Deployment

This project is configured for deployment on Netlify as a static site demonstration. Note that the full functionality requires a backend server.

### Deployment Steps

1. Fork this repository to your GitHub account
2. Sign up for Netlify (if you haven't already)
3. Create a new site in Netlify by connecting to your GitHub repository
4. Use the following build settings:
   - Build command: `python -c "import os; os.system('sh build.sh')"`
   - Publish directory: `staticfiles`
5. Click "Deploy site"

### Environment Variables (Optional)
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to 'False' for production

## Model Information
- Target Variable: Diabetic retinopathy prognosis (0: No, 1: Yes)
- Features:
  - Age: Patient's age
  - Systolic BP: Systolic blood pressure (Normal: < 120mmHg)
  - Diastolic BP: Diastolic blood pressure (Normal: < 80mmHg)
  - Cholesterol: Blood cholesterol level (Normal: 125-200 mg/dl) 