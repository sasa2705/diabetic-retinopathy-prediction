from django.core.management.base import BaseCommand
from prediction.models import Report
from prediction.views import generate_report_pdf
from datetime import datetime

class Command(BaseCommand):
    help = 'Regenerate all report PDFs with the latest template/style.'

    def handle(self, *args, **options):
        count = 0
        for report in Report.objects.all():
            patient = report.patient
            health_record = report.health_record
            prediction_result = bool(report.prediction)
            # Generate new PDF buffer
            buffer = generate_report_pdf(patient, health_record, prediction_result)
            # Overwrite the old PDF file
            report.pdf_file.save(f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf", buffer, save=True)
            count += 1
            self.stdout.write(self.style.SUCCESS(f'Regenerated report for test ID: {report.id}'))
        self.stdout.write(self.style.SUCCESS(f'Total reports regenerated: {count}')) 