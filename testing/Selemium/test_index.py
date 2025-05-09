from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ruta local del archivo HTML
file_path = "file:///C:/ruta/a/tu/login.html"  # Cambia esta ruta

# Inicializar el navegador (asegúrate de tener chromedriver en tu PATH)
driver = webdriver.Chrome()

try:
    driver.get(file_path)

    # Esperar a que cargue la página
    time.sleep(1)

    # Completar usuario y contraseña
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")

    # Enviar el formulario
    driver.find_element(By.TAG_NAME, "button").click()

    # Esperar mensaje
    time.sleep(1)

    mensaje = driver.find_element(By.ID, "mensaje").text
    print("Resultado del login:", mensaje)

finally:
    driver.quit()
