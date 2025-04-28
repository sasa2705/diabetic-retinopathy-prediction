from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import FileResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Patient, HealthRecord, Report, UserProfile
from .forms import PatientForm, HealthRecordForm, UserRegistrationForm
import joblib
import numpy as np
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
from reportlab.lib import colors
import os
from django.views.decorators.http import require_POST

def home(request):
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        patients = user_profile.patients.all()
    else:
        patients = []
    return render(request, 'prediction/home.html', {
        'patients': patients,
    })

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'prediction/register.html', {'form': form})

@login_required
def predict(request):
    user_profile = UserProfile.objects.get(user=request.user)
    patients = user_profile.patients.all()
    prediction_result = None

    if request.method == 'POST':
        existing_patient_id = request.POST.get('existing_patient_id')
        if existing_patient_id:
            # EXISTING PATIENT FLOW
            try:
                patient = Patient.objects.get(id=existing_patient_id)
            except Patient.DoesNotExist:
                messages.error(request, "Selected patient does not exist.")
                return redirect('predict')
            record_form = HealthRecordForm(request.POST)
            if record_form.is_valid():
                # Load model and scaler
                model = joblib.load('model.joblib')
                scaler = joblib.load('scaler.joblib')
                # Get form data
                age = record_form.cleaned_data['age']
                systolic_bp = record_form.cleaned_data['systolic_bp']
                diastolic_bp = record_form.cleaned_data['diastolic_bp']
                cholesterol = record_form.cleaned_data['cholesterol']
                # Make prediction
                input_data = np.array([[age, systolic_bp, diastolic_bp, cholesterol]])
                input_scaled = scaler.transform(input_data)
                prediction = model.predict(input_scaled)[0]
                # Save health record
                health_record = record_form.save(commit=False)
                health_record.patient = patient
                health_record.save()
                # Generate and save report
                report = generate_report(patient, health_record, bool(prediction))
                messages.success(request, 'Health record saved successfully!')
                prediction_result = report
            else:
                messages.error(request, "Please correct the errors in the health record form.")
            patient_form = PatientForm()  # Empty form for new patient
        else:
            # NEW PATIENT FLOW
            patient_form = PatientForm(request.POST)
            record_form = HealthRecordForm(request.POST)
            if patient_form.is_valid() and record_form.is_valid():
                patient, created = Patient.objects.get_or_create(
                    name=patient_form.cleaned_data['name'],
                    date_of_birth=patient_form.cleaned_data['date_of_birth']
                )
                if created:
                    patient.mobile_number = patient_form.cleaned_data['mobile_number']
                    patient.email = patient_form.cleaned_data['email']
                    patient.save()
                user_profile.patients.add(patient)
                model = joblib.load('model.joblib')
                scaler = joblib.load('scaler.joblib')
                age = record_form.cleaned_data['age']
                systolic_bp = record_form.cleaned_data['systolic_bp']
                diastolic_bp = record_form.cleaned_data['diastolic_bp']
                cholesterol = record_form.cleaned_data['cholesterol']
                input_data = np.array([[age, systolic_bp, diastolic_bp, cholesterol]])
                input_scaled = scaler.transform(input_data)
                prediction = model.predict(input_scaled)[0]
                health_record = record_form.save(commit=False)
                health_record.patient = patient
                health_record.save()
                report = generate_report(patient, health_record, bool(prediction))
                messages.success(request, 'Health record saved successfully!')
                prediction_result = report
            else:
                messages.error(request, "Please correct the errors in the forms.")
    else:
        patient_form = PatientForm()
        record_form = HealthRecordForm()

    return render(request, 'prediction/predict.html', {
        'patient_form': patient_form,
        'form': record_form,
        'patients': patients,
        'prediction_result': prediction_result
    })

@login_required
def download_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    # Check if user has access to this report
    user_profile = UserProfile.objects.get(user=request.user)
    if report.patient in user_profile.patients.all():
        return FileResponse(report.pdf_file, as_attachment=True)
    else:
        messages.error(request, 'You do not have permission to access this report.')
        return redirect('home')

@login_required
def patient_history(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    # Check if user has access to this patient
    user_profile = UserProfile.objects.get(user=request.user)
    if patient in user_profile.patients.all():
        health_records = patient.health_records.all().order_by('-created_at')
        reports = patient.reports.all().order_by('-created_at')
        return render(request, 'prediction/patient_history.html', {
            'patient': patient,
            'health_records': health_records,
            'reports': reports
        })
    else:
        messages.error(request, 'You do not have permission to access this patient\'s history.')
        return redirect('home')

def generate_report_pdf(patient, health_record, prediction_result):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    left = 50
    right = width - 50
    y = 750

    # Title with blue background
    p.setFillColor(colors.HexColor('#1976d2'))
    p.rect(0, y, width, 40, fill=1, stroke=0)
    p.setFillColor(colors.white)
    p.setFont("Helvetica-Bold", 22)
    p.drawString(left, y + 10, "Diabetic Retinopathy Prediction Report")
    y -= 60

    # Patient Information Box (compact)
    box_height = 75
    p.setFillColor(colors.HexColor('#f8f9fa'))
    p.roundRect(left-10, y-box_height+10, right-left+20, box_height, 10, fill=1, stroke=0)
    p.setFillColor(colors.HexColor('#1976d2'))
    p.setFont("Helvetica-Bold", 14)
    p.drawString(left, y, "Patient Information")
    p.setFillColor(colors.black)
    p.setFont("Helvetica-Bold", 11)
    p.drawString(left + 20, y - 18, "Name:")
    p.setFont("Helvetica", 11)
    p.drawString(left + 80, y - 18, f"{patient.name}")
    p.setFont("Helvetica-Bold", 11)
    p.drawString(left + 200, y - 18, "Date of Birth:")
    p.setFont("Helvetica", 11)
    p.drawString(left + 290, y - 18, f"{patient.date_of_birth}")
    p.setFont("Helvetica-Bold", 11)
    p.drawString(left + 20, y - 36, "Gender:")
    p.setFont("Helvetica", 11)
    p.drawString(left + 80, y - 36, f"{patient.get_gender_display()}")
    p.setFont("Helvetica-Bold", 11)
    p.drawString(left + 200, y - 36, "Mobile:")
    p.setFont("Helvetica", 11)
    p.drawString(left + 290, y - 36, f"{patient.mobile_number if patient.mobile_number else 'N/A'}")
    p.setFont("Helvetica-Bold", 11)
    p.drawString(left + 20, y - 54, "Email:")
    p.setFont("Helvetica", 11)
    p.drawString(left + 80, y - 54, f"{patient.email if patient.email else 'N/A'}")
    y -= (box_height + 10)

    # Health Record Box (compact)
    box_height = 60
    p.setFillColor(colors.HexColor('#f8f9fa'))
    p.roundRect(left-10, y-box_height+10, right-left+20, box_height, 10, fill=1, stroke=0)
    p.setFillColor(colors.HexColor('#1976d2'))
    p.setFont("Helvetica-Bold", 14)
    p.drawString(left, y, "Health Record")
    p.setFillColor(colors.black)
    p.setFont("Helvetica-Bold", 11)
    p.drawString(left + 20, y - 18, "Age:")
    p.setFont("Helvetica", 11)
    p.drawString(left + 60, y - 18, f"{health_record.age}")
    p.setFont("Helvetica-Bold", 11)
    p.drawString(left + 100, y - 18, "Systolic BP:")
    p.setFont("Helvetica", 11)
    p.drawString(left + 170, y - 18, f"{health_record.systolic_bp} mmHg")
    p.setFont("Helvetica-Bold", 11)
    p.drawString(left + 250, y - 18, "Diastolic BP:")
    p.setFont("Helvetica", 11)
    p.drawString(left + 330, y - 18, f"{health_record.diastolic_bp} mmHg")
    p.setFont("Helvetica-Bold", 11)
    p.drawString(left + 20, y - 36, "Cholesterol:")
    p.setFont("Helvetica", 11)
    p.drawString(left + 100, y - 36, f"{health_record.cholesterol} mg/dl")
    y -= (box_height + 10)

    # Prediction Result Box (compact, visible)
    box_height = 50
    p.setFillColor(colors.HexColor('#f8f9fa'))
    p.roundRect(left-10, y-box_height+10, right-left+20, box_height, 10, fill=1, stroke=0)
    p.setFillColor(colors.HexColor('#1976d2'))
    p.setFont("Helvetica-Bold", 14)
    p.drawString(left, y, "Prediction Result")
    if prediction_result:
        p.setFont("Helvetica-Bold", 13)
        p.setFillColor(colors.HexColor('#8B0000'))  # Maroon
        p.drawString(left + 20, y - 18, "HIGH RISK")
        p.setFillColor(colors.black)
        p.setFont("Helvetica-Bold", 11)
        p.drawString(left + 120, y - 18, "Patient shows signs of potential diabetic retinopathy")
    else:
        p.setFont("Helvetica-Bold", 13)
        p.setFillColor(colors.HexColor('#006400'))  # Green
        p.drawString(left + 20, y - 18, "LOW RISK")
        p.setFillColor(colors.black)
        p.setFont("Helvetica-Bold", 11)
        p.drawString(left + 120, y - 18, "Patient shows no significant signs of diabetic retinopathy")
    p.setFillColor(colors.black)
    y -= (box_height + 10)

    # Recommendations Box (compact)
    box_height = 70
    p.setFillColor(colors.HexColor('#f8f9fa'))
    p.roundRect(left-10, y-box_height+10, right-left+20, box_height, 10, fill=1, stroke=0)
    p.setFillColor(colors.HexColor('#1976d2'))
    p.setFont("Helvetica-Bold", 14)
    p.drawString(left, y, "Recommendations")
    p.setFillColor(colors.black)
    p.setFont("Helvetica", 11)
    bullet = u"\u2022"
    p.drawString(left + 20, y - 18, f"{bullet} Maintain a healthy weight")
    p.drawString(left + 20, y - 33, f"{bullet} Quit smoking if applicable")
    p.drawString(left + 20, y - 48, f"{bullet} Limit alcohol consumption")
    p.drawString(left + 220, y - 18, f"{bullet} Regular exercise (30 minutes daily)")
    p.drawString(left + 220, y - 33, f"{bullet} Monitor blood pressure regularly")

    p.save()
    buffer.seek(0)
    return buffer

def generate_report(patient, health_record, prediction_result):
    buffer = generate_report_pdf(patient, health_record, prediction_result)
    report = Report.objects.create(
        patient=patient,
        health_record=health_record,
        prediction=float(prediction_result)
    )
    report.pdf_file.save(f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf", buffer)
    return report

@require_POST
@login_required
def update_patient_info(request):
    patient_id = request.POST.get('patient_id')
    mobile = request.POST.get('mobile_number')
    email = request.POST.get('email')
    try:
        patient = Patient.objects.get(id=patient_id)
        user_profile = UserProfile.objects.get(user=request.user)
        if patient not in user_profile.patients.all():
            return JsonResponse({'success': False, 'error': 'Permission denied.'}, status=403)
        if mobile:
            patient.mobile_number = mobile
        if email:
            patient.email = email
        patient.save()
        return JsonResponse({'success': True})
    except Patient.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Patient not found.'}, status=404)
