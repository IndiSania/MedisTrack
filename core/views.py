from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect
from .models import Patient, Doctor, Appointment, Examination, Medicine

@login_required
def dashboard(request):
    context = {
        "patient_count": Patient.objects.count(),
        "doctor_count": Doctor.objects.filter(is_active=True).count(),
        "today_count": Appointment.objects.filter(date=date.today()).count(),
        "medicine_count": Medicine.objects.filter(is_active=True).count(),
        "recent_appointments": Appointment.objects.select_related("patient", "doctor").order_by("-date", "-time")[:6],
        "visit_stats": list(Appointment.objects.values("status").annotate(total=Count("id")).order_by("status")),
    }
    return render(request, "core/dashboard.html", context)

@login_required
def patients(request):
    q = request.GET.get("q", "").strip()
    data = Patient.objects.all().order_by("-created_at")
    if q:
        data = data.filter(name__icontains=q) | data.filter(medical_record__icontains=q)
    return render(request, "core/patients.html", {"patients": data, "q": q})

@login_required
def patient_add(request):
    if request.method == "POST":
        Patient.objects.create(
            medical_record=request.POST["medical_record"],
            name=request.POST["name"],
            birth_date=request.POST["birth_date"],
            gender=request.POST["gender"],
            phone=request.POST.get("phone", ""),
            address=request.POST.get("address", ""),
        )
        messages.success(request, "Data pasien berhasil ditambahkan.")
        return redirect("patients")
    return render(request, "core/patient_form.html")

@login_required
def doctors(request):
    return render(request, "core/doctors.html", {"doctors": Doctor.objects.all().order_by("name")})

@login_required
def appointments(request):
    data = Appointment.objects.select_related("patient", "doctor").order_by("-date", "-time")
    return render(request, "core/appointments.html", {"appointments": data})

@login_required
def appointment_add(request):
    if request.method == "POST":
        Appointment.objects.create(
            patient_id=request.POST["patient"],
            doctor_id=request.POST["doctor"],
            date=request.POST["date"],
            time=request.POST["time"],
            complaint=request.POST.get("complaint", ""),
        )
        messages.success(request, "Appointment berhasil dibuat.")
        return redirect("appointments")
    return render(request, "core/appointment_form.html", {
        "patients": Patient.objects.all().order_by("name"),
        "doctors": Doctor.objects.filter(is_active=True).order_by("name"),
    })

@login_required
def examinations(request):
    return render(request, "core/examinations.html", {
        "examinations": Examination.objects.select_related("appointment__patient", "appointment__doctor").order_by("-examined_at")
    })

@login_required
def medicines(request):
    return render(request, "core/medicines.html", {"medicines": Medicine.objects.all().order_by("name")})

@login_required
def reports(request):
    return render(request, "core/reports.html", {
        "patients": Patient.objects.count(),
        "appointments": Appointment.objects.count(),
        "examinations": Examination.objects.count(),
        "medicines": Medicine.objects.count(),
    })
