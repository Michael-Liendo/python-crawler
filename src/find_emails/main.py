from selenium import webdriver
from selenium.webdriver.common.by import By
import re

from utils.csv_save import load_urls_from_csv, save_emails_to_csv

driver = webdriver.Chrome()

# regex for matching email addresses
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$")


def get_emails_from_webs():
    emails = []

    # Stats
    total_pages = len(load_urls_from_csv())
    loaded_pages = []
    unloaded_pages = []
    total_emails = []

    for url in load_urls_from_csv():

        try:
            driver.get(url)
            loaded_pages.append(url)
        except:
            unloaded_pages.append(url)
            continue

        # Find all elements containing text on the page
        elements = driver.find_elements(By.XPATH, "//*[text()]")
        page_emails = []

        # Extract email addresses from text elements
        for element in elements:
            text = element.text
            matches = re.findall(EMAIL_REGEX, text)
            page_emails.extend(matches)

        total_emails.extend(page_emails)
        emails.extend(page_emails)

    # Print all stats
    print("Total pages:", total_pages)
    print("Loaded pages:", len(loaded_pages))
    print("Unloaded pages:", len(unloaded_pages))
    print("Total emails:", len(total_emails))

    return emails


def main():
    emails = get_emails_from_webs()
    save_emails_to_csv(emails)
