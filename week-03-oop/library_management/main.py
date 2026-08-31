from library import Library
from book import Book

library = Library()

while True:
    
    print("1. Add book")
    print("2. Find book")
    print("3. View books")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("book's name: ")
        author = input("book's author: ")
        book = Book(name, author)
        library.add(book)


    elif choice == "2":
        name = input("Book's name: ")
        print(library.find(name))

    elif choice == "3":
        library.view_books()
    elif choice == "4":
        exit()
