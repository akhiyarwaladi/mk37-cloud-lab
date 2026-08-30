from datetime import datetime
import os

# ====== KONFIGURASI ======
LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "jejak_waktu.log")

stempel = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG, "a") as f:          # "a" = tambah di akhir berkas
    f.write(stempel + "\n")
print("Tercatat pada", stempel)
