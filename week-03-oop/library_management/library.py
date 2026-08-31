class Library:
    def __init__(self):
        self.books = []

    def add (self,book):
        self.books.append(book)

    def find (self, name):
        for i in self.books:
            if i.name == name:
                return ("book found")
        return ("not found")

    def view_books (self):
        for i in self.books:
            print(i.show_info())