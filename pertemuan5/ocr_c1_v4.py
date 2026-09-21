import base64
import json
import sys
from pathlib import Path
import requests

# ====== KONFIGURASI ======
BASE_URL = "https://openrouter.ai/api/v1"
API_KEY = ""
MODEL = "inclusionai/ling-3.0-flash-vl:free"
# ========================

if not API_KEY:
    sys.exit("Isi API_KEY pada blok KONFIGURASI dulu.")
GAMBAR = "scan_c1/sirekap-1105072002001-2.jpg"
if len(sys.argv) > 1:
    GAMBAR = sys.argv[1]
path = Path(GAMBAR)
if not path.exists():
    sys.exit(f"Berkas {GAMBAR} tidak ada; "
             "jalankan unduh_sirekap_v2.py dulu.")

data = base64.b64encode(path.read_bytes()).decode()
respon = requests.post(
    f"{BASE_URL}/chat/completions",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={"model": MODEL,
          "messages": [{"role": "user", "content": [
              {"type": "text",
               "text": "Baca suara tiap calon. Jawab JSON: "
                       "suara_01, suara_02, suara_03. "
                       "Nilai integer atau null, bukan string. "
                       "Cocokkan angka dan terbilang. "
                       "X pengisi kosong; NIHIL = 0. "
                       "Tidak terlihat: null. Jangan menebak."},
              {"type": "image_url",
               "image_url": {"url": "data:image/jpeg;base64,"
                             + data}},
          ]}],
          "max_tokens": 2500,
          "reasoning": {"enabled": False}},
    timeout=120)
respon.raise_for_status()
pesan = respon.json()["choices"][0]["message"]
teks = pesan.get("content")
if not teks:
    sys.exit("Jawaban kosong; cek batas token/model.")
teks = teks.strip().removeprefix("```json")
teks = teks.removeprefix("```").removesuffix("```").strip()
hasil = json.loads(teks)
for k in ("suara_01", "suara_02", "suara_03"):
    n = hasil[k]
    if isinstance(n, str) and n.strip().isdecimal():
        hasil[k] = int(n)
print("Tipe hasil:", type(hasil).__name__)
for nomor in ("01", "02", "03"):
    print("Calon", nomor, ":", hasil[f"suara_{nomor}"])
angka = [hasil[f"suara_{n}"] for n in ("01", "02", "03")]
if all(type(n) is int and n >= 0 for n in angka):
    print("Jumlah tiga calon:", sum(angka))
else:
    print("Ada angka belum terbaca; periksa gambar.")
