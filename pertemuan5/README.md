# Pertemuan 5 - OCR C1 KPU

Kode untuk modul Pertemuan 5: pipeline OCR formulir C1 KPU (unduh terotomasi, arsip S3, RDS MySQL, model AI, cron). Ikuti berkas `_v1`, `_v2` sebelum versi lengkapnya. Kunci akses kelas disensor kosong pada repo ini.

| Berkas | Keterangan |
|---|---|
| `contoh_keluaran/jelajah_tps.txt` | Keluaran jelajah_tps.py: dua TPS pada kelurahan contoh. |
| `contoh_keluaran/kirim_s3.txt` | Contoh tiga objek Sirekap pada prefix TPS. |
| `contoh_keluaran/pipeline_lengkap.txt` | Keluaran pipeline_lengkap.py --simulasi: chart resmi, empat tahap per foto, rekap tuntas. |
| `contoh_keluaran/rds_isi_tabel.txt` | Contoh keluaran query kandidat dari JSON detail, data simulasi. |
| `contoh_keluaran/simpan_contoh.txt` | Keluaran normal simpan_contoh.py. |
| `contoh_keluaran/sirekap_tps.txt` | Keluaran unduh_sirekap.py untuk TPS contoh (hierarki, chart, tiga berkas). |
| `jelajah_tps.py` | Jelajah daftar TPS pada satu kelurahan dari JSON Sirekap (Langkah 1). |
| `kirim_s3.py` | Unggah tiga foto lokal TPS ke S3; integrasi unduh ada di Langkah 8. |
| `kirim_s3_v1.py` | Tangga 1 S3 (Langkah 3): klien boto3 dengan Access key ID + Secret, uji head_bucket. |
| `kirim_s3_v2.py` | Tangga 2 S3 (Langkah 3): unggah satu berkas dengan upload_file ke prefix terstruktur lalu verifikasi head_object. |
| `ocr_c1.py` | Tangga 5 OCR: fungsi kirim_ocr, validasi hasil, dan simulasi. |
| `ocr_c1_v1.py` | Tangga 1 OCR (Langkah 2): uji jalur API dengan pesan teks saja. |
| `ocr_c1_v2.py` | Tangga 2 OCR (Langkah 2): kirim satu gambar base64, jawaban mentah. |
| `ocr_c1_v3.py` | Tangga 3 OCR: minta JSON, periksa jawaban mentah. |
| `ocr_c1_v4.py` | Tangga 4 OCR: ubah JSON menjadi dict Python. |
| `pipeline_c1.py` | Tangga 2 pipeline (Langkah 7): OCR nyata + simpan RDS per berkas dari folder lokal. |
| `pipeline_c1_v1.py` | Tangga 1 pipeline (Langkah 7): loop seluruh scan_c1 dengan OCR tiruan, tanpa kunci AI. |
| `pipeline_lengkap.py` | Tugas akhir (Langkah 8): pipeline utuh satu loop, unduh KPU -> arsip S3 -> ekstraksi AI -> simpan RDS; ada mode --simulasi. |
| `pipeline_lengkap_v1.py` | Tugas akhir tangga 1 (Langkah 8): unduh foto dari URL KPU lalu LANGSUNG arsip S3, tanpa OCR/RDS. |
| `query_rds.py` | Periksa isi tabel hasil_ocr: SELECT dan cetak semua baris. |
| `simpan_contoh.py` | Contoh pemakaian: siapkan_tabel() dulu, satu hasil simulasi disimpan ke RDS. |
| `simpan_hasil_ai.py` | Simpan hasil OCR nyata foto Pilpres 2024 setelah latihan simulasi. |
| `simpan_rds.py` | Versi lengkap RDS (Langkah 5): tambah sambung() dan simpan() upsert idempoten. |
| `simpan_rds_v1.py` | Tangga 1 RDS (Langkah 5): buat database lalu tabel (IF NOT EXISTS), mode --dry. |
| `uji_ocr_bertahap.sh` | Urutan uji OCR Pilpres 2024, jalankan satu per satu. |
| `unduh_c1.py` | Versi lengkap unduh (Langkah 1): lewati bila sudah ada (idempoten) dan jeda sopan antar unduhan. |
| `unduh_c1_v1.py` | Tangga 1 unduh (Langkah 1): satu berkas untuk menguji jalur unduh. |
| `unduh_c1_v2.py` | Tangga 2 unduh (Langkah 1): perulangan kamus DAFTAR, tiga berkas, belum ada lewati. |
| `unduh_sirekap.py` | Versi lengkap Sirekap (Langkah 1): validasi tiap tingkat kode wilayah dan unduh semua foto (idempoten). |
| `unduh_sirekap_v1.py` | Tangga 1 Sirekap (Langkah 1): dua pertanyaan untuk membuktikan host dan bentuk data. |
| `unduh_sirekap_v2.py` | Tangga 2 Sirekap: unduh foto kedua (suara calon) TPS contoh. |
