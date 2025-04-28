#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from datetime import date
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'retinopathy_prediction.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def generate_report_pdf(patient, health_record, prediction_result):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    left = 50
    y = 750

    # Title (highlighted in blue)
    p.setFillColor(colors.HexColor('#1976d2'))
    p.rect(0, y, width, 40, fill=1, stroke=0)
    p.setFillColor(colors.white)
    p.setFont("Helvetica-Bold", 22)
    p.drawString(left, y + 10, "Diabetic Retinopathy Prediction Report")
    y -= 60

    p.setFillColor(colors.black)
    p.setFont("Helvetica-Bold", 13)
    p.drawString(left, y, "Patient Information")
    y -= 20
    p.setFont("Helvetica-Bold", 12)
    p.drawString(left, y, "Name:")
    p.setFont("Helvetica", 12)
    p.drawString(left + 80, y, f"{patient.name}")
    y -= 18
    p.setFont("Helvetica-Bold", 12)
    p.drawString(left, y, "Date of Birth:")
    p.setFont("Helvetica", 12)
    p.drawString(left + 100, y, f"{patient.date_of_birth}")
    y -= 18
    p.setFont("Helvetica-Bold", 12)
    p.drawString(left, y, "Mobile:")
    p.setFont("Helvetica", 12)
    p.drawString(left + 60, y, f"{patient.mobile_number if patient.mobile_number else 'N/A'}")
    y -= 18
    p.setFont("Helvetica-Bold", 12)
    p.drawString(left, y, "Email:")
    p.setFont("Helvetica", 12)
    p.drawString(left + 50, y, f"{patient.email if patient.email else 'N/A'}")
    y -= 30

    p.setFont("Helvetica-Bold", 13)
    p.drawString(left, y, "Health Record")
    y -= 20
    p.setFont("Helvetica-Bold", 12)
    p.drawString(left, y, "Age:")
    p.setFont("Helvetica", 12)
    p.drawString(left + 40, y, f"{health_record.age}")
    y -= 18
    p.setFont("Helvetica-Bold", 12)
    p.drawString(left, y, "Systolic BP:")
    p.setFont("Helvetica", 12)
    p.drawString(left + 80, y, f"{health_record.systolic_bp} mmHg")
    y -= 18
    p.setFont("Helvetica-Bold", 12)
    p.drawString(left, y, "Diastolic BP:")
    p.setFont("Helvetica", 12)
    p.drawString(left + 85, y, f"{health_record.diastolic_bp} mmHg")
    y -= 18
    p.setFont("Helvetica-Bold", 12)
    p.drawString(left, y, "Cholesterol:")
    p.setFont("Helvetica", 12)
    p.drawString(left + 80, y, f"{health_record.cholesterol} mg/dl")
    y -= 30

    p.setFont("Helvetica-Bold", 13)
    p.drawString(left, y, "Prediction Result")
    y -= 20
    p.setFont("Helvetica", 12)
    if prediction_result:
        p.setFillColor(colors.red)
        p.drawString(left, y, "High Risk - Patient shows signs of potential diabetic retinopathy")
    else:
        p.setFillColor(colors.green)
        p.drawString(left, y, "Low Risk - Patient shows no significant signs of diabetic retinopathy")
    p.setFillColor(colors.black)
    y -= 30

    p.setFont("Helvetica-Bold", 13)
    p.drawString(left, y, "Recommendations")
    y -= 20
    p.setFont("Helvetica", 12)
    p.drawString(left, y, "• Maintain a healthy weight")
    y -= 18
    p.drawString(left, y, "• Quit smoking if applicable")
    y -= 18
    p.drawString(left, y, "• Limit alcohol consumption")
    y -= 18
    # Add more recommendations as needed

    p.save()
    buffer.seek(0)
    return buffer


if __name__ == '__main__':
    main()
