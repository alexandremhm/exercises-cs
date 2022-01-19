import json
import csv


def books():
    with open("exdia.json") as file:
        books = []
        for line in file:
            books.append(json.loads(line))
        return books


listBooks = books()


book_categories = set()
for book in listBooks:
    for category in book["categories"]:
        book_categories.add(category)

percent_by_category = {category: 0 for category in book_categories}
total = 0

for book in listBooks:
    for category in book["categories"]:
        percent_by_category[category] += 1
        total += 1


for category in percent_by_category:
    percent_by_category[category] = (
        percent_by_category[category] / len(listBooks)
    ) * 100
    with open("book_categrories.csv", "w") as book_categories:
        writer = csv.writer(book_categories)
        header = ["categoria", "porcentagem"]

        writer.writerow(header)

        for category in percent_by_category.items():
            writer.writerow(category)

