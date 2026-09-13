from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ====== KONFIGURASI ======
URL_KANAL = "https://sport.detik.com/sepakbola"
BATAS = 3
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
d.get(URL_KANAL)
# Daftar artikel dimuat belakangan via JS: tunggu eksplisit, bukan sleep.
WebDriverWait(d, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="/d-"]')))
tautan = d.execute_script("""return [...new Set(
  [...document.querySelectorAll('a[href*="/d-"]')]
    .filter(a => a.href.includes('sepakbola'))
    .map(a => a.href))].slice(0, arguments[0]);""", BATAS)
print(f"Headline sepakbola: {len(tautan)}")
for u in tautan:
    print("-", u)
d.quit()
