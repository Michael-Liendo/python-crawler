from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.common.keys import Keys


class WebDriverSetUp:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()

    def get(self, url: str) -> None:
        try:
            self.driver = self.driver.get(url)
        except Exception as e:
            print(e)

    def find_elements(self, By: By, value: str) -> WDW:
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

        locator_method = LOCATOR_METHODS.get(By)
        return self.driver.find_element(locator_method, value)
