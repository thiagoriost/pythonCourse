class Book:
    def __init__(self, title, autor):
        self.title = title
        self.autor = autor
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title}, ha sido prestado")
        else:
            print(f"El libro {self.title}, no esta disponible")
    
    def return_book(self):
        self.available = True
        print(f"El libro {self.title}, ha sido devuelto")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} no esta disponible")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"El libro {book.title} ha sido devuelto")
        else:
            print(f"El libro {book.title} no esta en la lista de prestados")
            
class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_books(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado a la biblioteca")
    
    def remove_books(self, book):
        self.books.remove(book)
        print(f"El libro {book.title} ha sido eliminado de la biblioteca")
        
    def registrar_usuario(self, user):
        self.users.append(user)
        print(f"El usuario {user.name}, ha sido registrado")
    
    def show_avalaibable_books(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.autor}")
                

book1 = Book("TitleBook1", "Autor Rigo")
book2 = Book("TitleBook2", "Autor Ana")
book3 = Book("TitleBook3", "Autor Diego")

user1 = User("Rigo", 1234)

biblioteca = Library()
biblioteca.add_books(book1)
biblioteca.add_books(book2)
biblioteca.add_books(book3)
biblioteca.registrar_usuario(user1)
biblioteca.show_avalaibable_books()

user1.borrow_book(book1)
biblioteca.show_avalaibable_books()

user1.return_book(book1)
biblioteca.show_avalaibable_books()
