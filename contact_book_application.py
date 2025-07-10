def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contact")
    print("6. Exit")

def add_contact(contact_book):
    name = input("Enter contact name: ")
    if name in contact_book:
        print("Contact already exists!")
        return 
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact_book[name] = {"phone": phone, "email": email, "address": address}  
    print("Contact added successfully")

def view_contact(contact_book):
    name = input("Enter contact name: ")
    if name in contact_book:
        contact = contact_book[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input("Enter contact name: ")
    if name in contact_book:
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        if phone == '':
            phone = contact_book[name]['phone']
        if email == '':
            email = contact_book[name]['email']
        if address == '':
            address = contact_book[name]['address']
        
        contact_book[name] = {"phone": phone, "email": email, "address": address} 
        print("Contact updated successfully")
    else:
        print("Contact not found!") 

def delete_contact(contact_book):
    name = input("Enter contact name: ")
    if name in contact_book:
        del contact_book[name]
        print("contact deleted successfully")
    else:
        print("Contact not found!")

def List_all_contact(contact_book):
    if not contact_book:
        print("No contact available")
    else:
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print() # Blank line between contacts for readability

contact_book = {}

while True:
    display_menu()
    choice = input("Make your choice:")

    if choice == "1":
        add_contact(contact_book)
    elif choice == "2":
        view_contact(contact_book)
    elif choice == "3":
        edit_contact(contact_book)
    elif choice == "4":
        delete_contact(contact_book)
    elif choice == "5":
        List_all_contact(contact_book)
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again")





     