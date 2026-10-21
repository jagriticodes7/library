this is for testtt
from book import books, search_book

while True:
    print("\n--- Library Management System ---")
    print("1. Display books")
    print("2. Search book by title or ID")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for book in books:
            print(book)

    elif choice == "2":
        keyword = input("Enter book title or ID: ")
        results = search_book(keyword)

        if results:
            for book in results:
                print(book)
        else:
            print("Book not found.")

    elif choice == "3":
        break

    else:
        print("Invalid choice.")