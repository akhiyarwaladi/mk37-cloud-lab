import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# ====== KONFIGURASI ======
URL_KATALOG = "http://books.toscrape.com/"
# =========================

opsi = Options()
opsi.add_argument("--headless")
opsi.add_argument("--no-sandbox")
opsi.add_argument("--disable-dev-shm-usage")
opsi.add_argument("--window-size=1280,800")
d = webdriver.Chrome(options=opsi)
d.get(URL_KATALOG)
print("Halaman 1:", len(d.find_elements(By.CSS_SELECTOR, "article.product_pod")), "kartu")
d.save_screenshot("bukti_halaman1.png")
d.find_element(By.CSS_SELECTOR, "li.next a").click()
time.sleep(1)
print("Halaman 2:", len(d.find_elements(By.CSS_SELECTOR, "article.product_pod")), "kartu")
d.save_screenshot("bukti_halaman2.png")
pertama = d.find_elements(By.CSS_SELECTOR, "div.image_container img")[0]
print("Sampul pertama:", pertama.get_attribute("src"))
print("Bukti: bukti_halaman1.png + bukti_halaman2.png")
d.quit()
