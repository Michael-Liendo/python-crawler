from src.Pages.WebDriverSetup.DriverSetup import WebDriverSetUp

URL = "https://www.google.com/"


class HomePage:
    def __init__(self, wait: WebDriverSetUp.wait, enter: WebDriverSetUp.enter, driver: WebDriverSetUp) -> None:
        self.wait = wait
        self.key_enter = enter
        self.driver = driver

    # Elements
    search_button = "//textarea[@id='APjFqb']"

    def do_search(self, query: str) -> None:
        self.driver.get(URL)
        self.wait("XPATH", HomePage.search_button).send_keys(query)
        self.key_enter()
