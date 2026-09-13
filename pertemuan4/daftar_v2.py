from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# ====== KONFIGURASI ======
URL_KANAL = "https://bola.kompas.com/"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
# =========================

opsi = Options()
opsi.page_load_strategy = "eager"
opsi.add_argument("--headless")
opsi.add_argument("--no-sandbox")
opsi.add_argument("--disable-dev-shm-usage")
opsi.add_argument("--window-size=1280,800")
opsi.add_argument(f"--user-agent={UA}")
# Mode hemat: halaman Kompas terlalu berat bila gambar ikut dimuat.
opsi.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
d = webdriver.Chrome(options=opsi)
d.set_page_load_timeout(40)
d.get(URL_KANAL)
artikel = []
for a in d.find_elements(By.TAG_NAME, "a"):
    href = a.get_attribute("href") or ""
    if "kompas.com/read/" in href and href not in artikel:
        artikel.append(href)
    if len(artikel) == 5:
        break
print(f"Artikel Kompas Bola: {len(artikel)} contoh pertama")
for u in artikel:
    print("-", u)
d.quit()
