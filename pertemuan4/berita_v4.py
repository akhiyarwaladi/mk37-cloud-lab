from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ====== KONFIGURASI ======
URL_ARTIKEL = "https://sport.detik.com/sepakbola/uefa/d-8657802/bayern-munich-vs-bodo-glimt-die-roten-gasak-superlaget-5-0"
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
d.get(URL_ARTIKEL)
judul = d.execute_script("return document.querySelector('h1').innerText").strip()
gambar = d.execute_script("var i=document.querySelector('.detail__media img'); return i ? i.src : ''")
paragraf = d.execute_script(
    "return [...document.querySelectorAll('.detail__body-text p')]"
    ".map(p => p.innerText.trim()).filter(t => t.length > 0)")
print("Judul    :", judul)
print("Gambar   :", gambar[:100])
print("Paragraf :", len(paragraf))
print("Cuplikan :", paragraf[0][:120])
d.quit()
