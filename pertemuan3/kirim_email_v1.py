import smtplib
from email.message import EmailMessage
from app import ambil_cuaca

# ====== KONFIGURASI GMAIL ======
PENGIRIM = "EMAIL_GMAIL_ANDA@gmail.com"
SANDI    = "ISI_APP_PASSWORD_ANDA"   # App Password (16 karakter, tanpa spasi)
PENERIMA = "EMAIL_GMAIL_ANDA@gmail.com"
# ===============================

data = ambil_cuaca()
suhu = data["main"]["temp"]

pesan = EmailMessage()
pesan["Subject"] = f"Laporan Cuaca {data['name']}: {suhu} C"
pesan["From"]    = PENGIRIM
pesan["To"]      = PENERIMA
pesan.set_content(f"Suhu {data['name']} sekarang: {suhu} C. "
                  "Email otomatis dari instans EC2 - MK37.")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()               # enkripsi koneksi (TLS)
    smtp.login(PENGIRIM, SANDI)
    smtp.send_message(pesan)
print("Laporan berhasil dikirim ke", PENERIMA)
