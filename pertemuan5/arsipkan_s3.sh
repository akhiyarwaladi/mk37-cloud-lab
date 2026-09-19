#!/usr/bin/env bash
# ============================================================
# MK37 Pertemuan 5 - Arsip Scan C1 ke Amazon S3
# Ganti nama bucket dengan bucket milik Anda.
# Kode identik dengan modul PDF; kredensial diganti placeholder.
# ============================================================

# ---- Langkah 2: arsipkan scan ke S3 per sumber dan kode TPS ----
aws s3 cp scan_c1/ s3://mk37-namaanda-angkaunik/c1/kawalc1/ \
  --recursive --exclude "*" --include "c1-*"
aws s3 cp scan_c1/ \
  s3://mk37-namaanda-angkaunik/c1/sirekap/1105072002001/ \
  --recursive --exclude "*" --include "sirekap-*"
aws s3 ls s3://mk37-namaanda-angkaunik/c1/ --recursive

