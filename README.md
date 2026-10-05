# MedTrack — Clinic Management System

MedTrack adalah proyek sistem informasi klinik berbasis web yang dibuat menggunakan **Python + Django**. Proyek ini dirancang sebagai referensi portofolio PPLG dengan struktur aplikasi yang rapi dan mudah dikembangkan.

## Teknologi
- Python
- Django
- SQLite (default, mudah diganti PostgreSQL)
- HTML5
- CSS3
- JavaScript
- Chart.js

## Modul
- Dashboard statistik
- Manajemen pasien
- Data dokter
- Appointment
- Riwayat pemeriksaan
- Inventaris obat
- Laporan
- Django Admin
- Autentikasi pengguna

## Instalasi Windows

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Buka `http://127.0.0.1:8000/`.

## Akun
Gunakan akun superuser yang dibuat melalui:
```bash
python manage.py createsuperuser
```

## Struktur
- `medtrack/` konfigurasi proyek
- `core/` model, view, admin
- `templates/` antarmuka
- `static/` CSS dan aset
- `db.sqlite3` dibuat otomatis setelah migrasi

## Pengembangan lanjutan
Untuk versi produksi, tambahkan PostgreSQL, role permission yang lebih granular, audit log, export PDF/Excel, REST API, notifikasi, dan pengujian otomatis.

> Data kesehatan dalam proyek ini sebaiknya selalu menggunakan data fiktif untuk kebutuhan demo dan pembelajaran.
