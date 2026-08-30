import smtplib
from email.message import EmailMessage
from app import ambil_cuaca

# ====== KONFIGURASI GMAIL ======
PENGIRIM = "EMAIL_GMAIL_ANDA@gmail.com"
SANDI    = "ISI_APP_PASSWORD_ANDA"   # App Password (16 karakter, tanpa spasi)
PENERIMA = "EMAIL_GMAIL_ANDA@gmail.com"
# ===============================

def susun_pesan(data):
    kota    = data["name"]
    suhu    = data["main"]["temp"]
    terasa  = data["main"]["feels_like"]
    lembab  = data["main"]["humidity"]
    angin   = data["wind"]["speed"]
    kondisi = data["weather"][0]["description"].capitalize()

    pesan = EmailMessage()
    pesan["Subject"] = f"Laporan Cuaca {kota}: {suhu} C ({kondisi})"
    pesan["From"]    = PENGIRIM
    pesan["To"]      = PENERIMA

    # Versi teks biasa (fallback)
    pesan.set_content(f"""\
Berikut laporan cuaca terkini.

Kota       : {kota}
Kondisi    : {kondisi}
Suhu       : {suhu} C (terasa seperti {terasa} C)
Kelembaban : {lembab} %
Angin      : {angin} m/s

Email otomatis dari instans EC2 - MK37 Cloud Computing.
""")

    # Versi HTML (ditampilkan client modern)
    pesan.add_alternative(f"""\
<html>
  <body style="font-family: sans-serif">
    <h2 style="color:#003366">Laporan Cuaca {kota}</h2>
    <p style="font-size:2.2em; margin:0"><b>{suhu} °C</b> - {kondisi}</p>
    <p>Terasa seperti {terasa} °C | Kelembaban {lembab}%
       | Angin {angin} m/s</p>
    <hr>
    <small>Email otomatis dari instans EC2 -
      MK37 Cloud Computing, Universitas Jambi</small>
  </body>
</html>""", subtype="html")
    return pesan

def kirim(pesan):
    with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
        smtp.starttls()               # enkripsi koneksi (TLS)
        smtp.login(PENGIRIM, SANDI)
        smtp.send_message(pesan)

if __name__ == "__main__":
    kirim(susun_pesan(ambil_cuaca()))
    print("Laporan cuaca berhasil dikirim ke", PENERIMA)
