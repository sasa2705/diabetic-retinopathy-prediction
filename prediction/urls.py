from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='prediction/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('download-report/<int:report_id>/', views.download_report, name='download_report'),
    path('patient-history/<int:patient_id>/', views.patient_history, name='patient_history'),
    path('update-patient-info/', views.update_patient_info, name='update_patient_info'),
] 