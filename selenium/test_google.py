from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Crear una instancia del navegador
driver = webdriver.Chrome()

# Ir a Google
driver.get("https://www.google.com")

# Esperar 2 segundos (para que cargue)
time.sleep(2)

# Aceptar cookies si es necesario
try:
    driver.find_element(By.ID, "L2AGLb").click()
except:
    pass

# Encontrar el input de búsqueda y escribir
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Esperar y cerrar
time.sleep(5)
driver.quit()
