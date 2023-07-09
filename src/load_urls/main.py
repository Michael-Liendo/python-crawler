from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

from utils.csv_save import save_urls_to_csv

driver = webdriver.Chrome()


def get_urls_from_query(query, num_pages=1):
    contact_pages = []

    for page in range(num_pages):
        start = page * 10
        url = f"https://www.google.com/search?q={query}&start={start}&lr=lang_es"

        try:
            driver.get(url)
            print("Page loaded successfully")
        except:
            print("Can't load the page")
            driver.quit()
            exit(1)

        search_results = driver.find_elements(By.CSS_SELECTORm, "div.yuRUbf a")

        for result in search_results:
            url = result.get("href")
            if url.startswith("http"):
                contact_pages.append(url)

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
