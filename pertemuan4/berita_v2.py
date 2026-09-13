from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ====== KONFIGURASI ======
# Daftar kanal disalin dari menu homepage detik.com (MENU > Kategori Berita).
# Ditulis sebagai konstanta agar crawler deterministik dan cepat.
KANAL = {
    "news": "https://news.detik.com/",
    "sepakbola": "https://sport.detik.com/sepakbola",
    "seleb": "https://hot.detik.com/",
}
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
# =========================

opsi = Options()
opsi.page_load_strategy = "eager"
opsi.add_argument("--headless")
opsi.add_argument("--no-sandbox")
opsi.add_argument("--disable-dev-shm-usage")
opsi.add_argument("--window-size=1280,800")
opsi.add_argument(f"--user-agent={UA}")
d = webdriver.Chrome(options=opsi)
d.set_page_load_timeout(40)
print(f"Daftar kanal: {len(KANAL)}")
for nama, url in KANAL.items():
    d.get(url)
    print(f"- {nama:10s} {url}  => {d.title[:55]}")
d.quit()
