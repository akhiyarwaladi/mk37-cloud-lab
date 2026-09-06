# Pertemuan 5 - OCR C1 KPU

Kode untuk modul Pertemuan 4: integrasi instans EC2 (Pertemuan 3) dengan bucket Amazon S3.

| Berkas | Keterangan |
|---|---|
| `contoh_keluaran/simpan_contoh.txt` | Keluaran normal simpan_contoh.py. |
| `contoh_keluaran/sirekap_tps.txt` | Keluaran unduh_sirekap.py untuk TPS contoh (hierarki, chart, tiga berkas). |
| `ocr_c1.py` | Kirim gambar C1 ke model AI (OpenAI-compatible); ada mode --simulasi. |
| `pipeline_c1.py` | Pipeline penuh: proses semua gambar scan_c1 lalu simpan ke RDS. |
| `simpan_contoh.py` | Contoh pemakaian: satu hasil simulasi disimpan ke RDS. |
| `simpan_rds.py` | Skema tabel hasil_ocr, simpan idempoten (upsert), mode --dry. |
| `simpan_rds_v1.py` | Versi skema simpan_rds.py (Langkah 4): sambung dan buat tabel, mode --dry. |
| `unduh_c1.py` | Pengunduh formulir C1 dari arsip terbuka kawalc1 (idempoten, ada jeda). |
| `unduh_c1_v1.py` | Versi minimum unduh_c1.py (Langkah 1): satu berkas untuk menguji jalur unduh. |
| `unduh_sirekap.py` | Pengunduh foto C1 resmi Sirekap dari kode wilayah (cermin uji, idempoten, ada jeda). |
| `unduh_sirekap_v1.py` | Versi minimum Sirekap (Langkah 1): dua pertanyaan untuk membuktikan host dan bentuk data. |
