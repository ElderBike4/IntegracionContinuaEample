from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración del navegador
driver = webdriver.Chrome()

# Cargar la página web
driver.get("http://localhost:8081")

# Crear una instancia de WebDriverWait
wait = WebDriverWait(driver, 10)

try:
    # Esperar a que los campos num1 y num2 estén visibles
    num1 = wait.until(EC.visibility_of_element_located((By.ID, 'num1')))
    num2 = wait.until(EC.visibility_of_element_located((By.ID, 'num2')))
    resultado = wait.until(EC.visibility_of_element_located((By.ID, 'resultado')))

    # Ingresar valores
    num1.send_keys("10")
    num2.send_keys("5")

    # Probar suma
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Suma']"))).click()
    wait.until(EC.text_to_be_present_in_element((By.ID, 'resultado'), "15"))

    # Probar resta
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Resta']"))).click()
    wait.until(EC.text_to_be_present_in_element((By.ID, 'resultado'), "5"))

    # Probar multiplicación
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Multiplicar']"))).click()
    wait.until(EC.text_to_be_present_in_element((By.ID, 'resultado'), "50"))

finally:
    driver.quit()
