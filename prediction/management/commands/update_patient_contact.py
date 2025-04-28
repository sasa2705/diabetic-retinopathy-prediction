from django.core.management.base import BaseCommand, CommandError
from prediction.models import Patient

class Command(BaseCommand):
    help = 'Update a patient\'s mobile number and/or email by patient ID.'

    def add_arguments(self, parser):
        parser.add_argument('--id', type=int, required=True, help='Patient ID')
        parser.add_argument('--mobile', type=str, help='New mobile number')
        parser.add_argument('--email', type=str, help='New email address')

    def handle(self, *args, **options):
        patient_id = options['id']
        mobile = options.get('mobile')
        email = options.get('email')
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            raise CommandError(f'Patient with ID {patient_id} does not exist.')
        updated = False
        if mobile:
            patient.mobile_number = mobile
            updated = True
        if email:
            patient.email = email
            updated = True
        if updated:
            patient.save()
            self.stdout.write(self.style.SUCCESS(f'Updated patient {patient.name} (ID: {patient_id})'))
        else:
            self.stdout.write(self.style.WARNING('No updates provided. Use --mobile and/or --email.')) 