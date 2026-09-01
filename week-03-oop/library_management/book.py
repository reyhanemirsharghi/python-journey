class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def show_info(self):
        return f"Book Name: {self.name} | Author: {self.author}"

class EBook(Book):
    def __init__(self, name, author, file_size):
        super().__init__(name, author)
        self.file_size = file_size

    def show_info(self):
       return f"Book: {self.name}, Author: {self.author}, File size: {self.file_size}"
        
