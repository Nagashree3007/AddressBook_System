"""

@Author: Nagashree C R
@Date: 29-08-2024
@Last Modified by: Nagashree C R
@Last Modified: 29-08-2024
@Title: UC3-Ability to edit existing contact person using their Name

"""


#---UC1--Ability to create a Contacts in Address Book with first and last names, address, city, state, zip, phone number and email...

class Contact:
    #Represents a contact in the address book.
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def display_contact(self):
        """
        
        Definition:Display the details
        parameter:None
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
    
    Definition:Prompts the user for an integer input 
    parameter:None
    Return: returns the integer value.
    
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
#UC2--------Manages contacts in a specific address book.------------------------

class AddressBook:
    #Manages contacts in a single address book.
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        """
        
        Definition:Adds a new contact to the address book.
        
        parameter:contact details
        
        Return:None
        
        """
        if contact.first_name in self.contacts:
            print("Contact already exists.")
        else:
            self.contacts[contact.first_name] = contact
            print('----------------------------')
            print("Contact added successfully.")

#---------UC3---Ability to edit existing contact person using their name-----


    def update_and_display_contact(self, contact, field_name, new_value):
        """
        Updates a specific field of a contact and displays the updated contact details.
        
        Definition: Updates a specific field of the contact and prints the updated details.
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

    def edit_contact(self, name):
        """
        
        Definition:Edits an existing contact by name.
        parameter: name (str)-The name of the contact to be edited.
        Return: None (updates the contact's details).
        
        """
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

def main_menu(address_book):
    #Displays the main menu and handles user choices.
    while True:
        print("-------------------------------------------------")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Display Contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Enter contact details:")
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
        elif choice == "2":
            name = input("Enter the name of the contact to edit: ")
            address_book.edit_contact(name)
            
        elif choice == "3":
            print("\n-----------------Contacts in Address Book:------------")
            address_book.display_contacts()
        elif choice == "4":
            print("-------------------Exiting address book.------------------")
            break
        else:
            print("Invalid choice. Please try again.")

# Example usage
address_book = AddressBook()
main_menu(address_book)
