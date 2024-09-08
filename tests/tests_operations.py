from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Cargar la página web
driver.get("http://localhost:8080")

# Probar la suma
num1 = driver.find_element(By.ID, 'num1')
num2 = driver.find_element(By.ID, 'num2')
resultado = driver.find_element(By.ID, 'resultado')

# Ingresar valores
num1.send_keys("10")
num2.send_keys("5")

# Probar suma
driver.find_element(By.XPATH, "//button[text()='Suma']").click()
time.sleep(1)
assert resultado.text == "15"

# Probar resta
driver.find_element(By.XPATH, "//button[text()='Resta']").click()
time.sleep(1)
assert resultado.text == "5"

# Probar multiplicación
driver.find_element(By.XPATH, "//button[text()='Multiplicar']").click()
time.sleep(1)
assert resultado.text == "50"

driver.quit()
