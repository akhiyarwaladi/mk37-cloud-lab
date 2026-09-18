import base64
import os
import sys
from pathlib import Path
import requests

# ====== KONFIGURASI (environment variable) ======
BASE_URL = os.environ.get("OPENCODE_BASE_URL", "")
API_KEY = os.environ.get("OPENCODE_API_KEY", "")
MODEL = os.environ.get("OPENCODE_MODEL", "xiaomi-mimo-2.5")
# ================================================

if not BASE_URL or not API_KEY:
    sys.exit("Atur OPENCODE_BASE_URL dan OPENCODE_API_KEY dulu.")
GAMBAR = sys.argv[1] if len(sys.argv) > 1 else "scan_c1/c1-plano.jpeg"
path = Path(GAMBAR)
if not path.exists():
    sys.exit(f"Berkas {GAMBAR} tidak ada; jalankan unduh_c1.py dulu.")

data = base64.b64encode(path.read_bytes()).decode()
respon = requests.post(
    f"{BASE_URL}/chat/completions",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={"model": MODEL,
          "messages": [{"role": "user", "content": [
              {"type": "text",
               "text": "Apa isi gambar ini? Jawab dalam dua kalimat."},
              {"type": "image_url",
               "image_url": {"url": f"data:image/jpeg;base64,{data}"}},
          ]}],
          "max_tokens": 300},
    timeout=120)
respon.raise_for_status()
print(respon.json()["choices"][0]["message"]["content"].strip())
