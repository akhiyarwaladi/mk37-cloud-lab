#!/usr/bin/env bash
# ============================================================
# MK37 Pertemuan 3 - Bagian D: Laporan Email dan Cron (Langkah 15-18)
# Jalankan per baris sesuai urutan eksperimen Langkah 15-18 pada modul.
# Kode identik dengan modul PDF; kredensial diganti placeholder.
# ============================================================

# ---- Langkah 15: uji kirim manual (venv aktif) ----
python kirim_email.py

# ---- Langkah 17.2: jalankan manual sekali, lihat log ----
python3 waktu_logger.py
cat jejak_waktu.log

# ---- Langkah 17.4: periksa log setelah 3 menit ----
cat jejak_waktu.log

# ---- Langkah 17.5: hapus log lama sebelum uji jadwal */5 ----
rm jejak_waktu.log

# ---- Verifikasi: pastikan cron-lah yang mengeksekusi ----
date -u
grep CRON /var/log/syslog | tail -5

