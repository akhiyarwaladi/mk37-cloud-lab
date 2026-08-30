# Pertemuan 3 - Aplikasi Cuaca di EC2

Kode untuk modul Pertemuan 3: aplikasi cuaca end-to-end di Amazon EC2. Berkas program diletakkan di `~/weather-app/` pada instans Anda.

| Berkas | Keterangan |
|---|---|
| `app.py` | Program pengambil data cuaca OpenWeatherMap (Langkah 8). |
| `app_web.py` | Aplikasi web Flask dashboard cuaca (Langkah 10). |
| `kirim_email.py` | Pengirim laporan cuaca harian via Gmail SMTP/STARTTLS (Langkah 14). |
| `templates/dashboard.html` | Template Jinja2 halaman dashboard cuaca (Langkah 10). |
| `waktu_logger.py` | Pencatat stempel waktu untuk eksperimen membuktikan jadwal cron (Langkah 17). |
| `weatherapp.service` | Berkas unit systemd agar dashboard berjalan permanen (salin ke /etc/systemd/system/). |
