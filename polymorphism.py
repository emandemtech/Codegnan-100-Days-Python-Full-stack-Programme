# def add(x,y):                                        
#     return x+y                                       
# print(add(2,3))   #addition
# print(add("Hello ","World"))  #concatenation

# l = [1,2,3]
# s = {1,2,3}
# d = {1:'one', 2:'two', 3:'three'}
# t = (1,2,3)
# print(len(l))  #length of list
# print(len(s))  #length of set
# print(len(d))  #length of dictionary
# print(len(t))  #length of tuple

# method overriding:-

# class Shape:
#     def area(self):
#         pass
    
# class Rectangle(Shape):
#         def __init__(self, width, height):
#             self.width = width
#             self.height = height
#         def area(self):
#             print(super().area())
#             return self.width * self.height


# class Circle(Shape):
#         def __init__(self, radius):
#             self.radius = radius
#         def area(self):
#             print(super().area())
#             return 3.14 * self.radius ** 2

# r = Rectangle(5, 3)
# c = Circle(4)
# print("Area of Rectangle:", r.area())
# print("Area of Circle:", c.area())

#  method overloading:-

# class Calculator:
#     def add(self, a, b):
#         return a + b
    
#     def add(self, a, b, c):
#         return a + b + c
# calc = Calculator()
# #print(calc.add(2, 3))  # Output: 5          print(calc.add(2, 3))  # Output: 5 
# # TypeError: Calculator.add() missing 1 required positional argument: 'c'

# print(calc.add(2, 3, 4))  # Output: 9
# print(calc.add(2, 3, 0))  # Output: 5

# library managament:
# list of books, users

books = {1: {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "quantity": 10},
         2: {"title": "To Kill a Mockingbird", "author": "Harper Lee", "quantity": 5},
         3: {"title": "1984", "author": "George Orwell", "quantity": 15},
         4: {"title": "Pride and Prejudice", "author": "Jane Austen", "quantity": 20},
         5: {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "quantity": 25},
         6: {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "quantity": 5},
         7: {"title": "The Hobbit", "author": "J.R.R. Tolkien","quantity": 15},
         8: {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "quantity": 55},
         9: {"title": "Harry Potter and the Chamber of Secrets", "author": "J.K. Rowling", "quantity": 35},
         10: {"title": "Harry Potter and the Prisoner of Azkaban", "author": "J.K. Rowling", "quantity": 45}}

users = {1: {"name": "Alice", "borrowed_books": []},
         2: {"name": "Bob", "borrowed_books": []},
         3: {"name": "Charlie", "borrowed_books": []},
         4: {"name": "David", "borrowed_books": []},
         5: {"name": "Eve", "borrowed_books": []},
         6: {"name": "Frank", "borrowed_books": []},
         7: {"name": "Grace", "borrowed_books": []},
         8: {"name": "Heidi", "borrowed_books": []},
         9: {"name": "Ivan", "borrowed_books": []},
         10: {"name": "Judy", "borrowed_books": []}}


class Person:
    def __init__(self, name, pid):
        self.name = name
        self.id = pid


class Book:
    def __init__(self, bid, title, author):
        self.id = bid
        self.title = title
        self.author = author

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}"


class User(Person):
    def __init__(self, pid, name):
        super().__init__(name, pid)
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}'")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print("Book not found in borrowed list.")

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has not borrowed any books.")
        else:
            print(f"{self.name} borrowed:")
            for book in self.borrowed_books:
                print(f"- {book.get_info()}")


class Admin(Person):
    def __init__(self, pid, name):
        super().__init__(name, pid)
        self.books = {}   # book_id → [Book, quantity]

    def add_book(self, book, quantity=1):
        if book.id in self.books:
            self.books[book.id][1] += quantity
        else:
            self.books[book.id] = [book, quantity]
        print(f"Added {quantity} copies of '{book.title}'")

    def update_book_quantity(self, book_id, quantity):
        if book_id in self.books:
            self.books[book_id][1] += quantity
            print("Book quantity updated.")
        else:
            print("Book not found.")

    def remove_book_quantity(self, book_id, quantity):
        if book_id in self.books:
            if self.books[book_id][1] > quantity:
                self.books[book_id][1] -= quantity
                print("Quantity removed.")
            else:
                del self.books[book_id]
                print("Book completely removed from library.")
        else:
            print("Book not found.")

    def list_books(self):
        if not self.books:
            print("No books in library.")
        else:
            print("Books in library:")
            for book, qty in self.books.values():
                print(f"- {book.get_info()} (Quantity: {qty})")

    def list_users(self, users):
        print("Registered users:")
        for user in users:
            print(f"- {user.name} (ID: {user.id})")


def main():
    admin = Admin(1, "Admin")
    users = []

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book Quantity")
        print("3. Remove Book Quantity")
        print("4. List Books")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            qty = int(input("Quantity: "))
            book_id = len(admin.books) + 1
            book = Book(book_id, title, author)
            admin.add_book(book, qty)

        elif choice == "2":
            bid = int(input("Book ID: "))
            qty = int(input("Quantity to add: "))
            admin.update_book_quantity(bid, qty)

        elif choice == "3":
            bid = int(input("Book ID: "))
            qty = int(input("Quantity to remove: "))
            admin.remove_book_quantity(bid, qty)

        elif choice == "4":
            admin.list_books()

        elif choice == "5":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
