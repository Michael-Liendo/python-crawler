from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.common.keys import Keys

# Proxy and configs for setting up the driver.
from .Options import ArgumentOptions as AO, ExperimentalOptions as EO


class WebDriverSetUp:
    def __init__(self) -> None:
        s = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_argument(AO.START_MAXIMIZED)
        options.add_argument(AO.IGNORE_SSL_ERRORS)
        options.add_argument(AO.IGNORE_CERTIFICATE_ERRORS)
        options.add_argument(AO.UNDETECTED_CONTROL)
        # options.add_argument(AO.HEADLESS)
        options.add_experimental_option(EO.USE_AUTOMATION_EXT, False)
        options.add_experimental_option(EO.EXCLUDE_SWITCHES, EO.ENABLE_LOGGING)
        options.add_experimental_option(EO.EXCLUDE_SWITCHES, EO.ENALE_AUTOMATION)
        self.driver = webdriver.Chrome(service=s, options=options)

    def wait(self, signer: str, value: str) -> WDW:
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

        locator_method = LOCATOR_METHODS.get(signer)
        if not locator_method:
            raise ValueError(f"Invalid signer: {signer}")

        return WDW(self.driver, 10).until(
            EC.element_to_be_clickable((locator_method, value))
        )

    def search_decorator(method_name: str):
        def decorator(func):
            def wrapper(self, signer: str, value: str):
                LOCATOR_METHODS = {
                    "XPATH": By.XPATH,
                    "CLASS_NAME": By.CLASS_NAME,
                    "CSS_SELECTOR": By.CSS_SELECTOR,
                    "ID": By.ID,
                    "LINK_TEXT": By.LINK_TEXT,
                    "NAME": By.NAME,
                    "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
                    "TAG_NAME": By.TAG_NAME,
                }

                locator_method = LOCATOR_METHODS.get(signer)
                if not locator_method:
                    raise ValueError(f"Invalid signer: {signer}")

                method = getattr(self.driver, method_name)
                return method(locator_method, value)

            return wrapper

        return decorator

    @search_decorator("find_element")
    def find_element(self, signer: str, value: str):
        pass

    @search_decorator("find_elements")
    def find_elements(self, signer: str, value: str):
        pass

    def enter(self):
        return Keys.ENTER

    # Por ahora no se va a usar esta funcion, ya que solo se maneja una sola pestaña
    # def open_new_tab(self):
    #     driver = self.driver
    #     driver.send_keys(Keys.CONTROL + 't')

    def key_escape(self):
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
