phone_book = {}

def is_valid_number(number):
    return len(number) == 10 and number.isdigit()

def add_contact():
    name = input("Enter name: ")
    number = input("Enter number (10 digits): ")

    if is_valid_number(number):
        phone_book[name] = number
        print("Contact added successfully!")
    else:
        print("Invalid number! Must be exactly 10 digits.")

def update_contact():
    name = input("Enter name to update: ")
    if name in phone_book:
        number = input("Enter new number (10 digits): ")
        if is_valid_number(number):
            phone_book[name] = number
            print("Contact updated successfully!")
        else:
            print("Invalid number! Must be exactly 10 digits.")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in phone_book:
        del phone_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def search_contact():
    name = input("Enter name to search: ")
    if name in phone_book:
        print("Number:", phone_book[name])
    else:
        print("Contact not found!")

def menu():
    print("\nChoose an option:")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Number")
    print("5. Exit")

print("===================================")
print("   Welcome to Phone Book System")
print("===================================")

while True:
    menu()
    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        update_contact()
    elif choice == 3:
        delete_contact()
    elif choice == 4:
        search_contact()
    elif choice == 5:
        print("Thank you for using Phone Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1 to 5.")
