import csv


def save_urls_to_csv(data):
    with open('data/website.csv', 'w', encoding='utf-8', newline='') as f:

        writer = csv.DictWriter(f, fieldnames=["url"])
        writer.writeheader()

        for url in data:
            writer.writerow({"url": url})


def load_urls_from_csv():
    with open('data/website.csv', 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, fieldnames=["url"])
        data = [row["url"] for row in reader]
    data.pop(0)
    return data
