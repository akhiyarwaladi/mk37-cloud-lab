# Pertemuan 4 - Amazon S3

Kode untuk modul Pertemuan 4: integrasi instans EC2 (Pertemuan 3) dengan bucket Amazon S3.

| Berkas | Keterangan |
|---|---|
| `berita.py` | Rangkuman berita: 3 kanal x 3 artikel ke berita.json + img (Langkah 4). |
| `berita_v1.py` | Tangga 1 berita (Langkah 4): buka satu kanal detik.com. |
| `berita_v2.py` | Tangga 2 berita (Langkah 4): tabel 3 kanal news, sepakbola, seleb. |
| `berita_v3.py` | Tangga 3 berita (Langkah 4): tunggu eksplisit daftar headline. |
| `berita_v4.py` | Tangga 4 berita (Langkah 4): bedah satu artikel (judul, gambar, isi). |
| `contoh_keluaran/aws_configure.txt` | Isian jawaban perintah aws configure. |
| `contoh_keluaran/berita_py.txt` | Keluaran rangkuman berita (9 berita, 9 gambar). |
| `contoh_keluaran/berita_v2.txt` | Keluaran tangga 2 (3 kanal hidup). |
| `contoh_keluaran/berita_v3.txt` | Keluaran tangga 3 (3 headline sepakbola). |
| `contoh_keluaran/berita_v4.txt` | Keluaran tangga 4 (judul, gambar, 18 paragraf). |
| `contoh_keluaran/daftar_v1.txt` | Keluaran bedah 1 (judul kanal, 433 tautan). |
| `contoh_keluaran/daftar_v2.txt` | Keluaran bedah 2 (5 URL artikel Kompas). |
| `contoh_keluaran/daftar_v3.txt` | Keluaran bedah 3 (3 judul disorot). |
| `contoh_keluaran/galeri_py.txt` | Keluaran rangkuman galeri (40 sampul, 2 bukti). |
| `contoh_keluaran/galeri_v1.txt` | Keluaran tangga 1 (judul tab, 20 kartu). |
| `contoh_keluaran/galeri_v2.txt` | Keluaran tangga 2 (5 judul). |
| `contoh_keluaran/galeri_v3.txt` | Keluaran tangga 3 (20+20 kartu, 2 bukti). |
| `daftar_v1.py` | Bedah 1 daftar_artikel: hitung semua tautan kanal Kompas. |
| `daftar_v2.py` | Bedah 2 daftar_artikel: saring perulangan 5 URL artikel. |
| `daftar_v3.py` | Bedah 3 daftar_artikel: sorot kartu dan potret bukti. |
| `galeri_sampul.py` | Rangkuman galeri: fungsi, unduh 40 sampul idempoten (Langkah 4). |
| `galeri_sampul_v1.py` | Tangga 1 galeri (Langkah 4): buka halaman dan hitung kartu. |
| `galeri_sampul_v2.py` | Tangga 2 galeri (Langkah 4): tambah perulangan for, baca 5 judul. |
| `galeri_sampul_v3.py` | Tangga 3 galeri (Langkah 4): tambah klik next dan potret bukti. |
| `presign_url.sh` | Membuat presigned URL bermasa berlaku 10 menit (Langkah 5). |
| `siap_selenium.sh` | Siapkan Chromium dan pustaka Selenium di EC2 (Langkah 4). |
| `siap_selenium_windows.ps1` | Padanan setup Selenium di Windows PowerShell (Langkah 4). |
| `unggah_galeri.sh` | Sinkronisasi sampul/ dan bukti/ ke dua prefix S3 dan verifikasi jumlah (Langkah 4). |
