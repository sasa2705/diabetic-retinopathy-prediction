from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Patient, HealthRecord, UserProfile

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'date_of_birth', 'gender', 'mobile_number', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['age', 'systolic_bp', 'diastolic_bp', 'cholesterol']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '120'}),
            'systolic_bp': forms.NumberInput(attrs={'class': 'form-control', 'min': '60', 'max': '200'}),
            'diastolic_bp': forms.NumberInput(attrs={'class': 'form-control', 'min': '40', 'max': '120'}),
            'cholesterol': forms.NumberInput(attrs={'class': 'form-control', 'min': '100', 'max': '300'}),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number']
            )
        return user 