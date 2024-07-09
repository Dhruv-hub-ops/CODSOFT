contacts = {}

def display_menu():
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact {name} added successfully.")

def view_contacts():
    if contacts:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}\nPhone: {info['phone']}\nEmail:{info['email']}\nAddress:{info['address']}")
    else:
        print("No contacts found.")

def search_contact():
    search = input("Enter name or phone number to search: ")
    found = False
    for name, info in contacts.items():
        if search in [name, info['phone']]:
            print(f"Contact Found:\nName: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
