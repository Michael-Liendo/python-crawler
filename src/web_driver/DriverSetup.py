from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class WebDriverSetUp:
    _driver = None

    @classmethod
    def get_driver(cls):
        if not cls._driver:
            # Configurar las opciones del controlador Chrome
            chrome_options = Options()
            # Ejecutar en modo headless
            chrome_options.add_argument("--headless")
            cls._driver = webdriver.Chrome(options=chrome_options)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None

    @classmethod
    def get(cls, url: str) -> None:
        driver = cls.get_driver()
        try:
            driver.get(url)
        except Exception as e:
            print(e)

    @classmethod
    def find_element(cls, by: str, value: str):
        LOCATOR_METHODS = {
            "XPATH": By.XPATH,
            "CSS_SELECTOR": By.CSS_SELECTOR,
            "NAME": By.NAME,
            "ID": By.ID,
            "LINK_TEXT": By.LINK_TEXT,
            "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
            "TAG_NAME": By.TAG_NAME,
            "CLASS_NAME": By.CLASS_NAME,
        }

        locator_method = LOCATOR_METHODS.get(by)
        driver = cls.get_driver()
        return driver.find_element(locator_method, value)

    @classmethod
    def find_elements(cls, by: str, value: str):
        LOCATOR_METHODS = {
            "XPATH": By.XPATH,
            "CSS_SELECTOR": By.CSS_SELECTOR,
            "NAME": By.NAME,
            "ID": By.ID,
            "LINK_TEXT": By.LINK_TEXT,
            "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
            "TAG_NAME": By.TAG_NAME,
            "CLASS_NAME": By.CLASS_NAME,
        }

        locator_method = LOCATOR_METHODS.get(by)
        driver = cls.get_driver()
        return driver.find_elements(locator_method, value)
