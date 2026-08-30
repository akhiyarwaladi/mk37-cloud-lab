#!/usr/bin/env bash
# ============================================================
# MK37 Pertemuan 3 - Bagian C: Web Dashboard Flask (Langkah 10-12)
# Perintah pendukung; isi dashboard.html, app_web.py, dan weatherapp.service dari berkas terpisah.
# Kode identik dengan modul PDF; kredensial diganti placeholder.
# ============================================================

# ---- Langkah 10.1: pasang Flask (venv aktif) ----
pip install flask

# ---- Langkah 10.2: siapkan folder templates ----
mkdir templates
nano templates/dashboard.html

# ---- Langkah 11.1: jalankan server sementara untuk uji ----
python app_web.py

# ---- Langkah 12.1: sunting berkas unit systemd ----
sudo nano /etc/systemd/system/weatherapp.service

# ---- Langkah 12.2: aktifkan dan jalankan layanan ----
sudo systemctl daemon-reload
sudo systemctl enable --now weatherapp
sudo systemctl status weatherapp

