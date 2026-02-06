class BookManager:
    def __init__(self):
        self.books = {}
        self.borrowed = {}

    def add_book(self):
        bid = int(input("Enter book id: "))
        title = input("Enter book title: ")
        qty = int(input("Enter quantity: "))
        self.books[bid] = {"title": title, "qty": qty}
        print("Book added")

    def view_books(self):
        if not self.books:
            print("No books available")
            return
        print("\nAvailable Books:")
        for bid, info in self.books.items():
            print("ID:", bid, "Title:", info["title"], "Qty:", info["qty"])

    def borrow_book(self):
        bid = int(input("Enter book id to borrow: "))
        if bid in self.books and self.books[bid]["qty"] > 0:
            self.books[bid]["qty"] -= 1
            self.borrowed[bid] = self.borrowed.get(bid, 0) + 1
            print("Book borrowed")
        else:
            print("Book not available")

    def view_borrowed_books(self):
        if not self.borrowed:
            print("No borrowed books")
            return
        print("\nBorrowed Books:")
        for bid, qty in self.borrowed.items():
            print("ID:", bid, "Title:", self.books[bid]["title"], "Borrowed:", qty)

    def menu(self):
        while True:
            print("\n1. Add Book")
            print("2. View Books")
            print("3. Borrow Book")
            print("4. View Borrowed Books")
            print("5. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.view_books()
            elif choice == 3:
                self.borrow_book()
            elif choice == 4:
                self.view_borrowed_books()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice")

# Main
manager = BookManager()
manager.menu()
