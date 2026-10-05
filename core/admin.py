from django.contrib import admin
from .models import Doctor, Patient, Appointment, Examination, Medicine

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "specialty", "phone", "schedule", "is_active")
    search_fields = ("name", "specialty")

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("medical_record", "name", "gender", "birth_date", "phone")
    search_fields = ("medical_record", "name")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "date", "time", "status")
    list_filter = ("status", "date")
    search_fields = ("patient__name", "doctor__name")

@admin.register(Examination)
class ExaminationAdmin(admin.ModelAdmin):
    list_display = ("appointment", "diagnosis", "examined_at")
    search_fields = ("diagnosis", "appointment__patient__name")

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "stock", "unit", "price", "is_active")
    search_fields = ("name", "category")
