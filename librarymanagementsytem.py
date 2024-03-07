class book:
    #defining the attributes of the book
    def __init__(self, title, author,isbn,is_checked_out):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_checked_out=False


    #method to define if book is checked out
    def check_out(self):
        if not self.is_checked_out:
            print('book is checked out')
            return true
        else:
            print('book is not checked out')
    #return book is not checked out
    def return_book(self):
        if self.is_checked_out:
            print(f'you just returned{title}')
            return false
        else:
            print('you havent returned {title}')
            
            
    def _str_(self,my_book):
        return my_book(f"{title},{author},{isbn}")
        
#user input on the book
my_book=book(title=input('enter title of the book: '),
author=input('enter author of the book: '),
isbn=input('enter number of the book:',
is_checked_out=('enter "True" if book is checked out, and "False"is book is not checked out'))

print(my_book)

print(my_book.title)
print(my_book.author)
print(my_book.isbn)
print(my_book.is_checked_out)


#initializing a library with an empty list of books
#keeping record of all the books in the library
library class:
    def __init__(self):
        self.list_books=[]

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

    #

    #Prints a list of all books in the library, including their status (checked out or not).
    def list_books(self):
        return self.list_books

#initilaizing library
library=library()

creating a list of books
book1=book("The women", "Kristin Hannah",380)
book2=book("The House of Mirth" ,"Edith Wharton",678)
book3=book("The Start", "Edith Wharton",78)
book4=book("Absalom, Absalom!", "William Faulkner",90)
book5=book("the village", "John Waithaka",567)
#adding books to library
library.add_book
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

























