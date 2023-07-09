from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

from utils.csv_save import save_urls_to_csv
from web_driver import WebDriverSetUp


def get_urls_from_query(query, num_pages=1):
    contact_pages = []

    driver_setup = WebDriverSetUp()

    for page in range(num_pages):
        start = page * 10
        url = f"https://www.google.com/search?q={query}&start={start}&lr=lang_es"

        driver_setup.get(url)
        print("Page loaded successfully")

        search_results = driver_setup.find_elements(
            "CSS_SELECTOR", "div.yuRUbf a")

        for result in search_results:
            url = result.get("href")
            if url.startswith("http"):
                contact_pages.append(url)

    driver_setup.quit_driver()

    return contact_pages


def main():
    load_dotenv()

    # Change your finds query
    dorks_str = os.environ.get("DORKS")

    if dorks_str is None:
        print("La variable de entorno DORKS no está definida.")
        return

    dorks = dorks_str.split(", ")
    num_pages = int(os.environ.get("MAX_PAGES_NUMBS"))

    for dork in dorks:
        contact_pages = get_urls_from_query(dork, num_pages)
        print(f"Found {len(contact_pages)} contact pages:")
        save_urls_to_csv(contact_pages)
