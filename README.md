# MK37 Cloud Computing - Kode Praktikum

Repositori kode pendamping modul praktikum **MK37 Cloud Computing**
(Program Studi Informatika, Universitas Jambi):

- `pertemuan3/` - Pemanfaatan Amazon EC2 (OpenWeatherMap API,
  dashboard Flask, systemd, laporan email Gmail + cron)
- `pertemuan4/` - Penyimpanan Objek dengan Amazon S3 (bucket, AWS CLI,
  integrasi EC2 -> S3, presigned URL)

Panduan langkah demi langkah ada pada modul PDF masing-masing pertemuan;
isi berkas di sini identik dengan kotak kode pada modul.

## Catatan keamanan

Kredensial pada kode ini sengaja berupa **placeholder**:

| Placeholder | Ganti dengan |
|---|---|
| `ISI_API_KEY_ANDA` | API key OpenWeatherMap Anda (gratis: openweathermap.org/api) |
| `ISI_APP_PASSWORD_ANDA` | App Password 16 karakter Gmail Anda (butuh Verifikasi 2 Langkah) |
| `EMAIL_GMAIL_ANDA@gmail.com` | Alamat Gmail Anda |

Kunci demonstrasi kelas hanya dibagikan lewat jalur resmi kelas, tidak pernah
diunggah ke repositori publik.

## Cara memakai

1. Salin-tempel berkas yang diperlukan lewat tombol *Copy raw contents* di
   halaman GitHub, atau `git clone` repositori ini.
2. Untuk pertemuan 3, berkas ditempatkan di `~/weather-app/` pada instans EC2
   (lihat Langkah 7 modul); `weatherapp.service` disalin ke
   `/etc/systemd/system/`.
3. Entri crontab ada di `crontab_uji.txt` (eksperimen) dan
   `crontab_produksi.txt` (jadwal harian).
