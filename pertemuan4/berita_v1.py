from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ====== KONFIGURASI ======
URL_KANAL = "https://news.detik.com/"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
# =========================

opsi = Options()
opsi.page_load_strategy = "eager"  # cukup DOM, tak perlu tunggu iklan
opsi.add_argument("--headless")
opsi.add_argument("--no-sandbox")
opsi.add_argument("--disable-dev-shm-usage")
opsi.add_argument("--window-size=1280,800")
opsi.add_argument(f"--user-agent={UA}")
d = webdriver.Chrome(options=opsi)
d.set_page_load_timeout(40)
d.get(URL_KANAL)
print("Judul tab :", d.title)
d.quit()
