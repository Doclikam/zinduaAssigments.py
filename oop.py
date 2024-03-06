class book:
    #defining the attributes of the book
    def __init__(self, title, author,isbn,is_checked_out):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_checked_out=is_checked_out
    #method to define if book is checked out
    def check_out(self):
        if isbn=='True':
            return True
        else:
            return false

    def _str_(self,my_book):
        return str()(my_book)
        
#user input on the book
my_book=book(title=input('enter title of the book: '),
author=input('enter author of the book: '),
isbn=input('enter number of the book:'),
is_checked_out=('enter "True" if book is checked out, and "False"is book is not checked out'))



print(my_book.title)
print(my_book.author)
print(my_book.isbn)
print(my_book.is_checked_out)











