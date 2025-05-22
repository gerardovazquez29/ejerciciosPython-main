
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")  # Opcional: ejecutar sin interfaz gráfica
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
try:
    driver.get('https://escueladirecta.com/')
    elemento = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By. TAG_NAME, 'h1'))
    )
    print(elemento.text)
except Exception as e:
    print(f"Error durante el scraping: {e}")
finally:
    driver.quit()
