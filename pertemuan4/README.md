# Pertemuan 4 - Amazon S3

Kode untuk modul Pertemuan 4: integrasi instans EC2 (Pertemuan 3) dengan bucket Amazon S3.

| Berkas | Keterangan |
|---|---|
| `contoh_keluaran/aws_configure.txt` | Isian jawaban perintah aws configure. |
| `contoh_keluaran/galeri_py.txt` | Keluaran normal galeri_sampul.py (40 sampul idempoten, 2 bukti). |
| `contoh_keluaran/galeri_v1.txt` | Keluaran normal galeri_sampul_v1.py (judul tab, 20 kartu). |
| `contoh_keluaran/galeri_v2.txt` | Keluaran normal galeri_sampul_v2.py (5 sampul dan potret bukti). |
| `contoh_keluaran/kualitas_udara_py.txt` | Keluaran normal kualitas_udara.py (snapshot saat modul ditulis). |
| `galeri_sampul.py` | Scraper lengkap: klik next, unduh 40 sampul, potret 2 halaman (Langkah 4). |
| `galeri_sampul_v1.py` | Versi minimum scraper Selenium (Langkah 4): buktikan peramban hidup. |
| `galeri_sampul_v2.py` | Scraper 5 sampul pertama plus potret bukti halaman (Langkah 4). |
| `impor_kualitas_udara.py` | Satu baris impor untuk menggabungkan kualitas_udara ke kirim_email.py. |
| `kualitas_udara.py` | Versi lengkap tugas kabut asap: ambil_udara() PM2.5 Open-Meteo dan kategori ISPU. |
| `kualitas_udara_v1.py` | Versi minimum kualitas_udara (Tugas tambahan): lihat data mentah PM2.5. |
| `presign_url.sh` | Membuat presigned URL bermasa berlaku 10 menit (Langkah 5). |
| `siap_selenium.sh` | Siapkan Chromium dan pustaka Selenium di EC2 (Langkah 4). |
| `siap_selenium_windows.ps1` | Padanan setup Selenium di Windows PowerShell (Langkah 4). |
| `unggah_galeri.sh` | Sinkronisasi sampul/ dan bukti/ ke dua prefix S3 dan verifikasi jumlah (Langkah 4). |
