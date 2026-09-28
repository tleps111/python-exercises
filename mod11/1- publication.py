# Implement the following class hierarchy using Python: A publication can be either a book or a magazine. 
# Each publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor.
#  Also write the required initializers to both classes. Create a print_information method to both subclasses 
# for printing out all information of the publication in question. In the main program, 
# create publications Donald Duck (chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). 
# Print out all information of both publications using the methods you implemented.

class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"Chief editor: {self.chief_editor}")

book = Book("Compartment No. 6", "Rosa Liksom", 192)
magazine = Magazine("Donald Duck", "Aki Hyyppä")

book.print_information()
magazine.print_information()