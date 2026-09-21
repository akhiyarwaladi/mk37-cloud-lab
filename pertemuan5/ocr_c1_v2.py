import base64
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
               "text": "Apa isi gambar ini? "
                       "Jawab dalam dua kalimat."},
              {"type": "image_url",
               "image_url": {"url": "data:image/jpeg;base64,"
                             + data}},
          ]}],
          "max_tokens": 2500,
          "reasoning": {"enabled": False}},
    timeout=120)
respon.raise_for_status()
pesan = respon.json()["choices"][0]["message"]
print(pesan["content"].strip())
