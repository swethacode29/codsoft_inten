import pickle

# Load contacts from file
def load_contacts():
    try:
        with open('contacts.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open('contacts.pkl', 'wb') as file:
        pickle.dump(contacts, file)

# Display all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

# Add a new contact
def add_contact(contacts):
    name = input("Enter the contact's name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    
    phone = input("Enter the phone number: ").strip()
    email = input("Enter the email address: ").strip()
    address = input("Enter the address: ").strip()
    
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact {name} added successfully.")

# Search for a contact by name or phone number
def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ").strip()
    found = False
    
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
    
    if not found:
        print("No contact found.")

# Update a contact's details
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    
    print(f"Updating contact for {name}")
    phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
    email = input(f"Enter new email address (current: {contacts[name]['email']}): ").strip()
    address = input(f"Enter new address (current: {contacts[name]['address']}): ").strip()
    
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact {name} updated successfully.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

# Main menu
def main_menu():
    contacts = load_contacts()
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Exiting.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()
