from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.dashboard, name="dashboard"),
    path("patients/", views.patients, name="patients"),
    path("patients/add/", views.patient_add, name="patient_add"),
    path("doctors/", views.doctors, name="doctors"),
    path("appointments/", views.appointments, name="appointments"),
    path("appointments/add/", views.appointment_add, name="appointment_add"),
    path("examinations/", views.examinations, name="examinations"),
    path("medicines/", views.medicines, name="medicines"),
    path("reports/", views.reports, name="reports"),
]
