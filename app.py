from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Open the web
try:
    driver.get("https://novabitsve.com/")
    print("Page loaded")
except:
    print("Cannot open page")
    driver.quit()
    exit()

# Wait for the page to load
try:
    form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//form")))
except:
    print("No form")
    driver.quit()
    exit()

# find the form element
inputs_fields = form.find_elements(By.XPATH, "//input | //textarea")

# Fill all fields
for input_field in inputs_fields:
    name_attribute = input_field.get_attribute("name")

    if name_attribute == "name" or name_attribute == "nombre":
        input_field.send_keys("Novabits")

    elif name_attribute == "email" or name_attribute == "correo" or input_field.get_attribute("type") == "email":
        input_field.send_keys("contacto@novabitsve.com")

    else:
        try:
            input_field.send_keys("¡Hola! Soy de Novabits, una agencia especializada en desarrollo web. Estamos ofreciendo nuestros servicios para ayudar a negocios como el tuyo a tener una presencia en línea exitosa. Si estás interesado en una página web profesional y atractiva, contáctanos para discutir más detalles. ¡Espero tu respuesta!")
        except:
            pass

# Send form
try:
    form.submit()
    print("Submitted")
except:
    print("Cannot submit, try with click a button")
    button_field = form.find_element(By.XPATH, "//button")
    try:
        button_field.click()
    except:
        print("Cannot submit")

# Cerrar el controlador de Selenium
driver.quit()
