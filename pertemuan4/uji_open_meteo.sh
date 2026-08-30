#!/usr/bin/env bash
# ============================================================
# MK37 Pertemuan 4 - Tugas Tambahan: Uji API Kualitas Udara Open-Meteo
# Satu perintah curl untuk memastikan endpoint hidup; tidak butuh API key.
# Kode identik dengan modul PDF; kredensial diganti placeholder.
# ============================================================

# ---- Tugas tambahan: uji endpoint Open-Meteo Air Quality (tanpa API key) ----
curl -s "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=-1.61&longitude=103.61&current=pm2_5,pm10,carbon_monoxide&timezone=Asia%2FJakarta"

