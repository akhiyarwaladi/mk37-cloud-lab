# Pertemuan 3 - Aplikasi Cuaca di EC2

Kode untuk modul Pertemuan 3: aplikasi cuaca end-to-end di Amazon EC2. Berkas program diletakkan di `~/weather-app/` pada instans Anda.

| Berkas | Keterangan |
|---|---|
| `app.py` | Versi lengkap app.py (Langkah 8): fungsi ambil_cuaca, seluruh data, penanganan galat. |
| `app_v1.py` | Versi minimum app.py (Langkah 8): sebelas baris untuk menguji jalur API. |
| `app_web.py` | Aplikasi web Flask dashboard cuaca (Langkah 10). |
| `contoh_keluaran/api_respons.json` | Contoh respons JSON OpenWeatherMap (disingkat). |
| `contoh_keluaran/app_py.txt` | Keluaran normal python app.py (hasil uji nyata saat modul ditulis). |
| `contoh_keluaran/jejak_waktu_3menit.txt` | Isi jejak_waktu.log setelah tiga menit jadwal setiap menit. |
| `contoh_keluaran/jejak_waktu_5menit.txt` | Isi jejak_waktu.log dengan jadwal */5: tiga baris pada menit kelipatan lima. |
| `contoh_keluaran/jejak_waktu_manual.txt` | Isi jejak_waktu.log setelah satu eksekusi manual. |
| `contoh_keluaran/kirim_email_py.txt` | Keluaran normal python kirim_email.py. |
| `contoh_keluaran/ssh_verifikasi.txt` | Keluaran normal verifikasi SSH: whoami dan uname -a. |
| `kirim_email.py` | Versi lengkap kirim_email.py (Langkah 14): laporan terformat teks + HTML. |
| `kirim_email_v1.py` | Versi minimum kirim_email.py (Langkah 14): email teks polos. |
| `templates/dashboard.html` | Template Jinja2 halaman dashboard cuaca (Langkah 10). |
| `waktu_logger.py` | Pencatat stempel waktu untuk eksperimen membuktikan jadwal cron (Langkah 17). |
| `weatherapp.service` | Berkas unit systemd agar dashboard berjalan permanen (salin ke /etc/systemd/system/). |
