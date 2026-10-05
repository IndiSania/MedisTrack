from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=120)
    specialty = models.CharField(max_length=120)
    phone = models.CharField(max_length=30, blank=True)
    schedule = models.CharField(max_length=120, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.specialty}"

class Patient(models.Model):
    GENDER = [("L", "Laki-laki"), ("P", "Perempuan")]
    medical_record = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=120)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER)
    phone = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medical_record} - {self.name}"

class Appointment(models.Model):
    STATUS = [
        ("Menunggu", "Menunggu"), ("Diperiksa", "Diperiksa"),
        ("Selesai", "Selesai"), ("Dibatalkan", "Dibatalkan")
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS, default="Menunggu")
    complaint = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Examination(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    complaint = models.TextField()
    result = models.TextField()
    diagnosis = models.CharField(max_length=255)
    treatment = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    examined_at = models.DateTimeField(auto_now_add=True)

class Medicine(models.Model):
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=80)
    stock = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=30, default="pcs")
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
