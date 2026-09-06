#!/usr/bin/env bash
# ============================================================
# MK37 Pertemuan 4 - Langkah 3: Operasi CLI Inti S3
# Jalankan per baris sesuai urutan modul; mulai dari perintah baca-saja.
# Kode identik dengan modul PDF; kredensial diganti placeholder.
# ============================================================

# ---- Identitas dan daftar bucket (mulai dari yang hanya membaca) ----
# 1. Siapa saya? (identitas dari kredensial Anda)
aws sts get-caller-identity

# 2. Daftar bucket di akun ini
aws s3 ls

# ---- Roundtrip unggah, lihat, unduh, verifikasi identik ----
# 3. Unggah berkas (key = laporan/ec2-laporan.txt)
echo "Laporan cuaca dari EC2 - $(date)" > laporan.txt
aws s3 cp laporan.txt s3://mk37-namaanda-angkaunik/laporan/ec2-laporan.txt

# 4. Lihat isi bucket dan prefix
aws s3 ls s3://mk37-namaanda-angkaunik/
aws s3 ls s3://mk37-namaanda-angkaunik/laporan/

# 5. Unduh kembali dan buktikan identik
aws s3 cp s3://mk37-namaanda-angkaunik/laporan/ec2-laporan.txt ./cek-balik.txt
diff laporan.txt cek-balik.txt && echo "identik"

# ---- Sinkronisasi folder dan hapus objek ----
# 6. Siapkan folder contoh lalu sinkronisasi (mirip rsync)
mkdir -p data && echo "contoh 1" > data/jambi-01.txt
aws s3 sync ./data/ s3://mk37-namaanda-angkaunik/data/

# 7. Hapus objek
aws s3 rm s3://mk37-namaanda-angkaunik/laporan/ec2-laporan.txt

