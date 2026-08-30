# Pertemuan 5 - OCR C1 KPU

Kode untuk modul Pertemuan 4: integrasi instans EC2 (Pertemuan 3) dengan bucket Amazon S3.

| Berkas | Keterangan |
|---|---|
| `contoh_keluaran/simpan_contoh.txt` | Keluaran normal simpan_contoh.py. |
| `ocr_c1.py` | Kirim gambar C1 ke model AI (OpenAI-compatible); ada mode --simulasi. |
| `pipeline_c1.py` | Pipeline penuh: proses semua gambar scan_c1 lalu simpan ke RDS. |
| `simpan_contoh.py` | Contoh pemakaian: satu hasil simulasi disimpan ke RDS. |
| `simpan_rds.py` | Skema tabel hasil_ocr, simpan idempoten (upsert), mode --dry. |
| `unduh_c1.py` | Pengunduh formulir C1 dari arsip terbuka kawalc1 (idempoten, ada jeda). |
