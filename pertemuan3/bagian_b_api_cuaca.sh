#!/usr/bin/env bash
# ============================================================
# MK37 Pertemuan 3 - Bagian B: Mengambil Data Cuaca (Langkah 6-9)
# Jalankan per baris; langkah 6-7 dijalankan di server, ganti placeholder kunci Anda.
# Kode identik dengan modul PDF; kredensial diganti placeholder.
# ============================================================

# ---- Langkah 6.1: perbarui paket dan pasang prasyarat Python ----
sudo apt update
sudo apt install -y python3-venv python3-pip curl

# ---- Langkah 6.2: uji API dengan curl (ganti ISI_API_KEY_ANDA) ----
curl -s "https://api.openweathermap.org/data/2.5/weather?q=Jambi,ID&appid=ISI_API_KEY_ANDA&units=metric&lang=id"

# ---- Langkah 7: folder proyek dan virtual environment ----
mkdir ~/weather-app && cd ~/weather-app
python3 -m venv venv
source venv/bin/activate      # prompt berubah: (venv) ...
pip install requests

# ---- Langkah 9: jalankan app.py (dari ~/weather-app, venv aktif) ----
python app.py

