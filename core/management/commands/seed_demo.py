from django.core.management.base import BaseCommand
from core.models import Doctor, Patient, Appointment, Medicine
from datetime import date, time

class Command(BaseCommand):
    help = "Mengisi data demo MedTrack"

    def handle(self, *args, **options):
        doctors = [
            ("dr. Aulia Pratama", "Dokter Umum", "081200000001", "Senin - Jumat, 08.00 - 14.00"),
            ("dr. Nabila Putri", "Dokter Anak", "081200000002", "Senin - Kamis, 09.00 - 15.00"),
            ("dr. Reza Mahendra", "Penyakit Dalam", "081200000003", "Selasa - Jumat, 10.00 - 16.00"),
        ]
        for x in doctors:
            Doctor.objects.get_or_create(name=x[0], defaults={"specialty":x[1],"phone":x[2],"schedule":x[3]})

        patients = [
            ("RM-0001","Nadia Permata","2005-03-14","P","081300000001","Semarang"),
            ("RM-0002","Raka Wijaya","2003-08-21","L","081300000002","Jepara"),
            ("RM-0003","Salsa Maharani","2006-01-09","P","081300000003","Kudus"),
            ("RM-0004","Dimas Prakoso","2004-11-27","L","081300000004","Demak"),
            ("RM-0005","Alya Safitri","2002-06-05","P","081300000005","Pati"),
        ]
        for x in patients:
            Patient.objects.get_or_create(medical_record=x[0], defaults={"name":x[1],"birth_date":x[2],"gender":x[3],"phone":x[4],"address":x[5]})

        meds = [
            ("Paracetamol 500mg","Analgesik",85,"tablet",1500),
            ("Amoxicillin 500mg","Antibiotik",42,"kapsul",2500),
            ("Cetirizine 10mg","Antihistamin",18,"tablet",1800),
            ("Oralit","Rehidrasi",65,"sachet",1000),
            ("Vitamin B Complex","Vitamin",30,"tablet",2200),
        ]
        for x in meds:
            Medicine.objects.get_or_create(name=x[0], defaults={"category":x[1],"stock":x[2],"unit":x[3],"price":x[4]})

        d = list(Doctor.objects.all())
        p = list(Patient.objects.all())
        if d and p and not Appointment.objects.exists():
            for i in range(5):
                Appointment.objects.create(patient=p[i % len(p)], doctor=d[i % len(d)], date=date.today(), time=time(8+i,30), complaint="Pemeriksaan rutin.")

        self.stdout.write(self.style.SUCCESS("Data demo MedTrack berhasil dibuat."))
