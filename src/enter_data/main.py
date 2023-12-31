from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.csv_save import load_urls_from_csv
from web_driver.DriverSetup import WebDriverSetUp


def main():
    # Open the web
    urls = load_urls_from_csv()

    # Statistics
    total_pages = len(urls)
    loaded_pages = []
    unloaded_pages = []
    total_send_pages = []
    total_unsent_pages = []

    driver_setup = WebDriverSetUp()

    for url in urls:
        driver_setup.get(url)
        loaded_pages.append(url)

        # Wait for the page to load
        try:
            form = WebDriverWait(driver_setup.get_driver(), 10).until(
                EC.presence_of_element_located((By.XPATH, "//form")))
        except:
            unloaded_pages.append(url)
            total_unsent_pages.append(url)
            continue

        # find the form element
        inputs_fields = form.find_elements(By.XPATH, "//input | //textarea")

        # Fill all fields
        for input_field in inputs_fields:
            try:
                name_attribute = input_field.get_attribute("name") or ''
            except:
                pass

            if name_attribute == "name" or name_attribute == "nombre":
                input_field.send_keys("Novabits")

            elif name_attribute == "phone" or name_attribute == "telefono" or (input_field.get_attribute("type") or '') == "tel":
                input_field.send_keys("0000000000")

            # subject
            elif name_attribute == "subject" or name_attribute == "subject":
                input_field.send_keys("Propuesta de desarrollo")

            elif name_attribute == "email" or name_attribute == "correo" or (input_field.get_attribute("type") or '') == "email":
                input_field.send_keys("contacto@novabitsve.com")

            else:
                try:
                    input_field.send_keys("¡Hola! Soy de Novabits, una agencia especializada en desarrollo web. Estamos ofreciendo nuestros servicios para ayudar a negocios como el tuyo a tener una presencia en línea exitosa. Si estás interesado en una página web profesional y atractiva, contáctanos para discutir más detalles. ¡Espero tu respuesta!")
                except:
                    pass

        # Send form
        try:
            form.submit()
            total_send_pages.append(url)
        except:
            button_field = form.find_element(By.XPATH, "//button")
            try:
                button_field.click()
                total_send_pages.append(url)
            except:
                total_unsent_pages.append(url)

    driver_setup.quit_driver()

    # Print all stats
    print("Total pages: ", total_pages)
    print("Loaded pages: ", len(loaded_pages))
    print("Unloaded pages: ", len(unloaded_pages))
    print("Total send pages: ", len(total_send_pages))
    print("Total unsent pages: ", len(total_unsent_pages))
