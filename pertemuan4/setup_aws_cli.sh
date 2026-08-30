#!/usr/bin/env bash
# ============================================================
# MK37 Pertemuan 4 - Langkah 3: Siapkan AWS CLI di Instans EC2
# Jalankan berurutan dari sesi SSH instans Pertemuan 3.
# Kode identik dengan modul PDF; kredensial diganti placeholder.
# ============================================================

# ---- Langkah 3.1: SSH ke instans (cek IP terbaru di Console) ----
ssh -i ~/Downloads/mk37-keypair-namaanda.pem ubuntu@18.139.xx.xx

# ---- Langkah 3.2: pasang AWS CLI ----
sudo apt update && sudo apt install -y awscli
aws --version

# ---- Langkah 3.3: konfigurasikan kredensial ----
aws configure

