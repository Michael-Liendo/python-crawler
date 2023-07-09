from src.Pages.GooglePages.HomePage import HomePage
from src.Pages.WebDriverSetup.DriverSetup import WebDriverSetUp


class Runner(WebDriverSetUp):
    def __init__(self) -> None:
        super().__init__()
        self.home_page = HomePage(wait=self.wait, enter=self.enter, driver=self.driver)

    def run(self) -> None:
        self.home_page.do_search("Hello World")


if __name__ == "__main__":
    runner = Runner()
    runner.run()
