#!/usr/bin/env bash
# ============================================================
# MK37 Pertemuan 3 - Bagian A: Mengakses Instans EC2 (Langkah 5)
# Jalankan per baris sesuai urutan modul, bukan sekaligus.
# Kode identik dengan modul PDF; kredensial diganti placeholder.
# ============================================================

# ---- Langkah 5.1: beri izin akses kunci privat (di laptop) ----
# macOS / Linux
chmod 400 ~/Downloads/mk37-keypair-namaanda.pem

# ---- Langkah 5.2: hubungkan ke instans (ganti dengan IP publik Anda) ----
ssh -i ~/Downloads/mk37-keypair-namaanda.pem ubuntu@18.139.xx.xx

# ---- Verifikasi setelah masuk server ----
whoami && uname -a

