from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import re

from utils.csv_save import load_urls_from_csv, save_emails_to_csv
from web_driver.DriverSetup import WebDriverSetUp

# regex for matching email addresses
EMAIL_REGEX = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")


def get_emails_from_webs():
    emails = []

    # Stats
    total_pages = len(load_urls_from_csv())
    loaded_pages = []
    unloaded_pages = []
    total_emails = []

    driver_setup = WebDriverSetUp()

    for url in load_urls_from_csv():
        driver_setup.get(url)
        loaded_pages.append(url)

        # Find all elements containing text on the page
        elements = driver_setup.find_elements("XPATH", "//*[text()]")
        page_emails = []

        # Extract email addresses from text elements
        for element in elements:
            try:
                text = element.text
                matches = re.findall(EMAIL_REGEX, text)
                page_emails.extend(matches)
            except StaleElementReferenceException:
                continue

        total_emails.extend(page_emails)
        emails.extend(page_emails)

    driver_setup.quit_driver()

    # Print all stats
    print("Total pages:", total_pages)
    print("Loaded pages:", len(loaded_pages))
    print("Unloaded pages:", len(unloaded_pages))
    print("Total emails:", len(total_emails))

    return emails


def main():
    emails = get_emails_from_webs()
    save_emails_to_csv(emails)
