import csv

def save_to_csv(data, file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Page Name', 'Page URL', 'Page Likes', 'Page Category', 'Page Description'])
        writer.writerows(data)
        
def load_from_csv(file_name):
    with open(file_name, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    return data
