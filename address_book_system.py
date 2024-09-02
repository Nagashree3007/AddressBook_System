"""

@Author: Nagashree C R
@Date: 29-08-2024
@Last Modified by: Nagashree C R
@Last Modified: 29-08-2024
@Title: UC10-Ability to get number of contact persons i.e. count by City or State

"""

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def __eq__(self, other):
        return isinstance(other, Contact) and (self.first_name, self.last_name) == (other.first_name, other.last_name)

    def __hash__(self):
        return hash((self.first_name, self.last_name))

    def display_contact(self):
        return (f"Name: {self.first_name} {self.last_name}\n"
                f"Address: {self.address}\n"
                f"City: {self.city}\n"
                f"State: {self.state}\n"
                f"Zip Code: {self.zip_code}\n"
                f"Phone Number: {self.phone_number}\n"
                f"Email: {self.email}\n")

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

class AddressBook:
    def __init__(self):
        self.contacts = {}
        self.city_dict = {}
        self.state_dict = {}

    def add_contact(self, contact):
        if contact.first_name in self.contacts:
            existing_contact = self.contacts[contact.first_name]
            if existing_contact == contact:
                print("Contact already exists.")
                return
        
        self._update_contact_dictionaries(contact)
        self.contacts[contact.first_name] = contact
        print('----------------------------')
        print("Contact added successfully.")

    def _update_contact_dictionaries(self, contact):
        if contact.first_name in self.contacts:
            old_contact = self.contacts[contact.first_name]
            if old_contact.city in self.city_dict:
                self.city_dict[old_contact.city].remove(old_contact)
            if old_contact.state in self.state_dict:
                self.state_dict[old_contact.state].remove(old_contact)
        
        if contact.city not in self.city_dict:
            self.city_dict[contact.city] = set()
        self.city_dict[contact.city].add(contact)

        if contact.state not in self.state_dict:
            self.state_dict[contact.state] = set()
        self.state_dict[contact.state].add(contact)

    def update_contact(self, name, field_name, new_value):
        if name not in self.contacts:
            print("Contact not found.")
            return
        
        contact = self.contacts[name]
        if field_name == "address":
            contact.address = new_value
        elif field_name == "city":
            if contact.city in self.city_dict:
                self.city_dict[contact.city].remove(contact)
            contact.city = new_value
            if contact.city not in self.city_dict:
                self.city_dict[contact.city] = set()
            self.city_dict[contact.city].add(contact)
        elif field_name == "state":
            if contact.state in self.state_dict:
                self.state_dict[contact.state].remove(contact)
            contact.state = new_value
            if contact.state not in self.state_dict:
                self.state_dict[contact.state] = set()
            self.state_dict[contact.state].add(contact)
        elif field_name == "zip_code":
            contact.zip_code = new_value
        elif field_name == "phone_number":
            contact.phone_number = new_value
        elif field_name == "email":
            contact.email = new_value
        else:
            print("Invalid field.")
            return

        print("\n-----------------Updated Contact Details:------------")
        print(contact.display_contact())
        print("-----------------------------------------------------")

    def delete_contact(self, name):
        if name in self.contacts:
            contact = self.contacts.pop(name)
            if contact.city in self.city_dict:
                self.city_dict[contact.city].remove(contact)
                if not self.city_dict[contact.city]:
                    del self.city_dict[contact.city]
            if contact.state in self.state_dict:
                self.state_dict[contact.state].remove(contact)
                if not self.state_dict[contact.state]:
                    del self.state_dict[contact.state]
            print(f"Contact '{name}' has been deleted.")
        else:
            print("Contact not found.")

    def edit_contact(self, name):
        if name not in self.contacts:
            print("Contact not found.")
            return
        
        contact = self.contacts[name]
        while True:
            print(f"\nEditing contact details for {name}")
            print("1. Address")
            print("2. City")
            print("3. State")
            print("4. ZIP Code")
            print("5. Phone Number")
            print("6. Email")
            print("7. Exit Editing")
            choice = input("Enter the number of the detail to edit (1-7): ")

            if choice == "1":
                new_value = input("New address: ")
                self.update_contact(name, "address", new_value)
            elif choice == "2":
                new_value = input("New city: ")
                self.update_contact(name, "city", new_value)
            elif choice == "3":
                new_value = input("New state: ")
                self.update_contact(name, "state", new_value)
            elif choice == "4":
                new_value = get_integer_input("New ZIP code: ")
                self.update_contact(name, "zip_code", new_value)
            elif choice == "5":
                new_value = get_integer_input("New phone number: ")
                self.update_contact(name, "phone_number", new_value)
            elif choice == "6":
                new_value = input("New email: ")
                self.update_contact(name, "email", new_value)
            elif choice == "7":
                print("Exiting edit mode.")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts.values():
                print(contact.display_contact())

    def view_contacts_by_city(self, city):
        contacts = self.city_dict.get(city, None)
        if contacts:
            print(f"Contacts in {city} ({len(contacts)}):")
            for contact in contacts:
                print(contact.display_contact())
        else:
            print(f"No contacts found in {city}.")
        print(f"Total contacts in {city}: {len(contacts) if contacts else 0}")

    def view_contacts_by_state(self, state):
        contacts = self.state_dict.get(state, None)
        if contacts:
            print(f"Contacts in {state} ({len(contacts)}):")
            for contact in contacts:
                print(contact.display_contact())
        else:
            print(f"No contacts found in {state}.")
        print(f"Total contacts in {state}: {len(contacts) if contacts else 0}")

class AddressBookManager:
    def __init__(self):
        self.address_books = {}

    def add_address_book(self, name):
        if name in self.address_books:
            print("Address book with this name already exists.")
        else:
            self.address_books[name] = AddressBook()
            print(f"Address book '{name}' added successfully.")

    def get_address_book(self, name):
        return self.address_books.get(name, None)

def main_menu(manager):
    selected_address_book = None
    
    while True:
        print("-------------------------------------------------\n")
        print("1. Add Address Book")
        print("2. Select Address Book")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name of the new address book: ")
            manager.add_address_book(name)
        elif choice == "2":
            if not manager.address_books:
                print("No address books available.")
                continue

            print("Available Address Books:")
            for index, name in enumerate(manager.address_books.keys(), start=1):
                print(f"{index}. {name}")

            index = get_integer_input("Enter the number of the address book to select: ") - 1
            names = list(manager.address_books.keys())

            if 0 <= index < len(names):
                selected_name = names[index]
                selected_address_book = manager.get_address_book(selected_name)
                print(f"Selected Address Book: {selected_name}")
                address_book_menu(selected_address_book)
            else:
                print("Invalid selection. Please try again.")
        elif choice == "3":
            print("-------------------Exiting system.------------------")
            break
        else:
            print("Invalid choice. Please try again.")

def address_book_menu(address_book):
    while True:
        print("-------------------------------------------------\n")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. View Contacts by City")
        print("6. View Contacts by State")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                print("\nEnter contact details:")
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                address = input("Address: ")
                city = input("City: ")
                state = input("State: ")
                zip_code = get_integer_input("ZIP Code: ")
                phone_number = get_integer_input("Phone Number: ")
                email = input("Email: ")

                contact = Contact(
                    first_name=first_name,
                    last_name=last_name,
                    address=address,
                    city=city,
                    state=state,
                    zip_code=zip_code,
                    phone_number=phone_number,
                    email=email
                )

                address_book.add_contact(contact)

                another = input("Do you want to add another contact? (yes/no): ").strip().lower()
                if another != 'yes':
                    break
        elif choice == "2":
            if not address_book.contacts:
                print("No contacts available to edit.")
            else:
                name = input("Enter the name of the contact to edit: ")
                address_book.edit_contact(name)
        elif choice == "3":
            if not address_book.contacts:
                print("No contacts available to delete.")
            else:
                name = input("Enter the name of the contact to delete: ")
                address_book.delete_contact(name)
        elif choice == "4":
            print("\n-----------------Contacts in Address Book:------------")
            address_book.display_contacts()
        elif choice == "5":
            city = input("Enter city to view contacts: ")
            address_book.view_contacts_by_city(city)
        elif choice == "6":
            state = input("Enter state to view contacts: ")
            address_book.view_contacts_by_state(state)
        elif choice == "7":
            print("Exiting address book menu.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = AddressBookManager()
    main_menu(manager)
