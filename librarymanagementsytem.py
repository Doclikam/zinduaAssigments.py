class book:
    #defining the attributes of the book
    def __init__(self, title, author,isbn,is_checked_out):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_checked_out=False

    #method to define if book is checked out
    def check_out(self):
        return True
    
    def return_book(self):
        return False
        
    def __str__(self):
        return (f"title: {self.title}, author: {self.author}, isbn: {self.isbn}")
        
#user input on the book
my_book=book("The women", "Kristin Hannah",380)


print(my_book.check_out())
print(my_book.return_book())
print(my_book.__str__())

#initializing a library with an empty list of books
#keeping record of all the books in the library
class library:
    def __init__(self):
        self.list_book=[]

    #Adding a Book object to the library's book list.
    def add_book(self,book):
        self.list_books.append(book)
        

    #Removes a book from the library by ISBN. If the book is not found, print an error message.
    def remove_book(self, isbn):
        for book in self.list_books:
            if book.isbn==isbn:
                self.books.remove(book)
            else:
                print('book not in library')


    #Checks out a book by ISBN. If the book is already checked out, print an error message.
    def check_out_book(self, isbn):
        for book in self.list_books:
            if book.isbn==isbn and book.is_checked_out==False:
                self.list_books.remove(book)
                print(f'you have borrowed {title}. return it in 30 days')
                return True
            else:
                print('book already checked out')
                return false


    #Returns a book by ISBN. If the book is not found or is not checked out, print an error message
    def return_book(self, isbn): 
        for book in self.list_books:
            if book.isbn==isbn and book.is_checked_out==True:
                self.list_books.append(book)
                print(f'thankyou for returning {title}')
            else:
                if book.is_checked_out==False:
                    print('book was not checked out')
                else:
                    print('book not in library')

    #Prints a list of all books in the library, including their status (checked out or not).
    def list_books(self):
        return self.list_books


mylibrary=library()

#initilaizing library
library=library()

#creating a list of books
book1=library("The women", "Kristin Hannah",380)
book2=library("The House of Mirth" ,"Edith Wharton",678)
book3=library("The Start", "Edith Wharton",78)
book4=library("Absalom, Absalom!", "William Faulkner",90)
book5=library("the village", "John Waithaka",567)
#adding books to library

mylibrary.add_book(book1)
mylibrary.add_book(book2)
mylibrary.add_book(book3)
mylibrary.add_book(book4)
mylibrary.add_book(book5)


print(books.add_book())
print(books.check_out_book())
print(books.return_book())
print(list_books())

























