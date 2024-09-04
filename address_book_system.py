"""
@Author: Nagashree C R
@Date: 29-08-2024
@Last Modified by: Nagashree C R
@Last Modified: 29-08-2024
@Title: UC8-Ability to search Person in a City or State across multiple Address Books
"""

class Contact:
    # Represents a contact in the address book.
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
        """
        Definition: Overrides the equality operator to compare contacts based on their full name.
        Parameter: other (Contact) - The contact to compare with.
        Return: True if both contacts have the same first and last name, else False.
        """
        if isinstance(other, Contact):
            return (self.first_name, self.last_name) == (other.first_name, other.last_name)
        return False

    def __hash__(self):
        """
        Definition: Overrides the hash function to allow the Contact class to be used in sets and dictionaries.
        Return: Hash value based on first and last names.
        """
        return hash((self.first_name, self.last_name))

    def display_contact(self):
        """
        Definition: Display the details of the contact.
        Parameter: None
        Return: Returns a formatted string of the contact's details.
        """
        return (f"Name: {self.first_name} {self.last_name}\n"
                f"Address: {self.address}\n"
                f"City: {self.city}\n"
                f"State: {self.state}\n"
                f"Zip Code: {self.zip_code}\n"
                f"Phone Number: {self.phone_number}\n"
                f"Email: {self.email}\n")

def get_integer_input(prompt):
    """
    Definition: Prompts the user for an integer input.
    Parameter: prompt (str) - The prompt message to display.
    Return: Returns the integer value entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

class AddressBook:
    # Manages contacts in a single address book.
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        """
        Definition: Adds a new contact to the address book if it does not already exist.
        Parameter: contact (Contact) - The contact to add.
        Return: None
        """
        if contact.first_name in self.contacts:
            existing_contact = self.contacts[contact.first_name]
            if existing_contact == contact:
                print("Contact already exists.")
                return
        self.contacts[contact.first_name] = contact
        print('----------------------------')
        print("Contact added successfully.")

    def update_and_display_contact(self, contact, field_name, new_value):
        """
        Definition: Updates a specific field of a contact and displays the updated contact details.
        Parameter: contact (Contact) - The contact to update.
                   field_name (str) - The field to update.
                   new_value (str or int) - The new value for the field.
        Return: None
        """
        if field_name == "address":
            contact.address = new_value
        elif field_name == "city":
            contact.city = new_value
        elif field_name == "state":
            contact.state = new_value
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
        """
        Definition: Deletes the contact with the given name.
        Parameter: name (str) - The name of the contact to delete.
        Return: None
        """
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' has been deleted.")
        else:
            print("Contact not found.")

    def edit_contact(self, name):
        """
        Definition: Edits an existing contact by name.
        Parameter: name (str) - The name of the contact to be edited.
        Return: None (updates the contact's details).
        """
        if not self.contacts:
            print("No contacts available to edit.")
            return

        if name in self.contacts:
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
                    new_address = input("New address: ")
                    self.update_and_display_contact(contact, "address", new_address)
                elif choice == "2":
                    new_city = input("New city: ")
                    self.update_and_display_contact(contact, "city", new_city)
                elif choice == "3":
                    new_state = input("New state: ")
                    self.update_and_display_contact(contact, "state", new_state)
                elif choice == "4":
                    new_zip_code = get_integer_input("New ZIP code: ")
                    self.update_and_display_contact(contact, "zip_code", new_zip_code)
                elif choice == "5":
                    new_phone_number = get_integer_input("New phone number: ")
                    self.update_and_display_contact(contact, "phone_number", new_phone_number)
                elif choice == "6":
                    new_email = input("New email: ")
                    self.update_and_display_contact(contact, "email", new_email)
                elif choice == "7":
                    print("Exiting edit mode.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Contact not found.")

    def display_contacts(self):
        """
        Definition: Displays all contacts in the address book.
        Parameter: None
        Return: None
        """
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts.values():
                print(contact.display_contact())

    def search_by_city(self, city):
        """
        Definition: Searches for contacts in the specified city.
        Parameter: city (str) - The city to search for.
        Return: List of contacts in the specified city.
        """
        return [contact for contact in self.contacts.values() if contact.city.lower() == city.lower()]

    def search_by_state(self, state):
        """
        Definition: Searches for contacts in the specified state.
        Parameter: state (str) - The state to search for.
        Return: List of contacts in the specified state.
        """
        return [contact for contact in self.contacts.values() if contact.state.lower() == state.lower()]

class AddressBookManager:
    def __init__(self):
        self.address_books = {}

    def add_address_book(self, name):
        """
        Definition: Adds a new address book with the given name.
        Parameter: name (str) - The name of the address book.
        Return: None
        """
        if name in self.address_books:
            print("Address book with this name already exists.")
        else:
            self.address_books[name] = AddressBook()
            print(f"Address book '{name}' added successfully.")

    def get_address_book(self, name):
        """
        Definition: Retrieves the address book with the given name.
        Parameter: name (str) - The name of the address book.
        Return: AddressBook - The address book associated with the name.
        """
        return self.address_books.get(name, None)

    def search_all_address_books(self, city=None, state=None):
        """
        Definition: Searches for contacts in all address books based on city or state.
        Parameter: city (str) - The city to search for.
                   state (str) - The state to search for.
        Return: List of contacts matching the city or state criteria.
        """
        results = []
        for address_book in self.address_books.values():
            if city:
                results.extend(address_book.search_by_city(city))
            if state:
                results.extend(address_book.search_by_state(state))
        return results

def main_menu(manager):
    """
    Definition: Displays options to the user and processes their choice.
    Parameter: manager (AddressBookManager) - The address book manager.
    Return: None
    """
    while True:
        print("-------------------------------------------------\n")
        print("1. Add Address Book")
        print("2. Select Address Book")
        print("3. Search Contacts")
        print("4. Exit")
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
                address_book = manager.get_address_book(selected_name)
                if address_book:
                    address_book_menu(address_book)
            else:
                print("Invalid selection. Please try again.")
        elif choice == "3":
            search_menu(manager)
        elif choice == "4":
            print("-------------------Exiting system.------------------")
            break
        else:
            print("Invalid choice. Please try again.")

def address_book_menu(address_book):
    """
    Definition: Displays options to manage the selected address book.
    Parameter: address_book (AddressBook) - The selected address book.
    Return: None
    """
    while True:
        print("-------------------------------------------------\n")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")
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

                # Check if the user wants to add another contact
                another = input("Do you want to add another contact? (yes/no): ").strip().lower()
                if another != 'yes':
                    break
        elif choice == "2":
            if not address_book.contacts:
                print('--------------------------------')
                print("No contacts available to edit.")
            else:
                name = input("Enter the name of the contact to edit: ")
                address_book.edit_contact(name)
        elif choice == "3":
            if not address_book.contacts:
                print('--------------------------------')
                print("No contacts available to delete.")
            else:
                name = input("Enter the name of the contact to delete: ")
                address_book.delete_contact(name)
        elif choice == "4":
            print("\n-----------------Contacts in Address Book:------------")
            address_book.display_contacts()
        elif choice == "5":
            print("-------------------Exiting address book.------------------")
            break
        else:
            print("Invalid choice. Please try again.")

def search_menu(manager):
    """
    Definition: Provides options to search contacts in all address books.
    Parameter: manager (AddressBookManager) - The address book manager.
    Return: None
    """
    while True:
        print("-------------------------------------------------\n")
        print("1. Search by City")
        print("2. Search by State")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter the city to search: ")
            results = manager.search_all_address_books(city=city)
            if results:
                print("\n--- Search Results by City ---")
                for contact in results:
                    print(contact.display_contact())
            else:
                print("No contacts found in the specified city.")
        elif choice == "2":
            state = input("Enter the state to search: ")
            results = manager.search_all_address_books(state=state)
            if results:
                print("\n--- Search Results by State ---")
                for contact in results:
                    print(contact.display_contact())
            else:
                print("No contacts found in the specified state.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

# Initialize AddressBookManager and start main menu
address_book_manager = AddressBookManager()
main_menu(address_book_manager)
