books = [
    {"id": 101, "title": "Python Basics", "author": "John Smith"},
    {"id": 102, "title": "Learning Git", "author": "David Lee"},
    {"id": 103, "title": "Data Structures", "author": "Alice Brown"}
]


def search_book(keyword):
    results = []

    for book in books:
        if (keyword.lower() in book["title"].lower()
                or keyword == str(book["id"])):
            results.append(book)

    return results