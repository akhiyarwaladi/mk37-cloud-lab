#!/usr/bin/env bash
# ============================================================
# MK37 Pertemuan 5 - Kredensial RDS dan Pustaka Klien
# Tambahkan baris export ke ~/.bashrc agar tetap hidup antar sesi.
# Kode identik dengan modul PDF; kredensial diganti placeholder.
# ============================================================

# ---- Langkah 4: kredensial RDS pada env var + pustaka pymysql ----
source ~/weather-app/venv/bin/activate
pip install pymysql
export RDS_HOST="mk37-c1-db.xxxxx.ap-southeast-3.rds.amazonaws.com"
export RDS_USER="admin"
export RDS_PASSWORD="kata-sandi-anda"
export RDS_DB="mk37c1"

