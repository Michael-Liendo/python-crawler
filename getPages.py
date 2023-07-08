import requests
from bs4 import BeautifulSoup


def get_contact_pages(query, num_pages=1):
    contact_pages = []

    for page in range(num_pages):
        start = page * 10
        url = f"https://www.google.com/search?q={query}&start={start}&lr=lang_es"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        search_results = soup.select("div.yuRUbf a")

        for result in search_results:
            url = result.get("href")
            if url.startswith("http"):
                contact_pages.append(url)

    return contact_pages


def main():
    dorks = ["inurl:contacto.php"]
    num_pages = 30

    for dork in dorks:

        contact_pages = get_contact_pages(dork, num_pages)
        print(f"Found {len(contact_pages)} contact pages:")
        for page in contact_pages:
            print(page)
        print()


if __name__ == "__main__":
    main()
