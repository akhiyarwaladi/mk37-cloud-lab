# Pertemuan 3 - Aplikasi Cuaca di EC2

Kode untuk modul Pertemuan 3: aplikasi cuaca end-to-end di Amazon EC2. Berkas program diletakkan di `~/weather-app/` pada instans Anda.

| Berkas | Keterangan |
|---|---|
| `app.py` | Versi lengkap app.py (Langkah 8): fungsi ambil_cuaca, seluruh data, penanganan galat. |
| `app_v1.py` | Versi minimum app.py (Langkah 8): sebelas baris untuk menguji jalur API. |
| `app_web.py` | Aplikasi web Flask dashboard cuaca (Langkah 10). |
| `kirim_email.py` | Versi lengkap kirim_email.py (Langkah 14): laporan terformat teks + HTML. |
| `kirim_email_v1.py` | Versi minimum kirim_email.py (Langkah 14): email teks polos. |
| `templates/dashboard.html` | Template Jinja2 halaman dashboard cuaca (Langkah 10). |
| `waktu_logger.py` | Pencatat stempel waktu untuk eksperimen membuktikan jadwal cron (Langkah 17). |
| `weatherapp.service` | Berkas unit systemd agar dashboard berjalan permanen (salin ke /etc/systemd/system/). |
