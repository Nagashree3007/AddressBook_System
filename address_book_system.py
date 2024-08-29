'''
    @Author:Nagashree C R
    @Date: 29-08-2024
    @Last Modified by:Nagashree C R
    @Last Modified: 29-08-2024
    @Title : UC2-Ability to add a new Contact to Address Book

'''
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
        return (
            f"Name: {self.first_name} {self.last_name}\n"
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

# Collecting user input
print("Enter contact details:")
first_name = input("First Name: ")
last_name = input("Last Name: ")
address = input("Address: ")
city = input("City: ")
state = input("State: ")
zip_code = get_integer_input("ZIP Code: ")
phone_number = get_integer_input("Phone Number: ")
email = input("Email: ")

# Creating a Contact object with the user-provided details
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


#Manages contacts in a specific address book.
class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = {}

    def add_contact(self, contact):
        """
        
        Definition:Adds a new contact to the address book.
        
        parameter:contact details
        
        Return:None
        
        """
        self.contacts[contact.first_name] = contact
        print("Contact added successfully.")

#
address_book = AddressBook(name="MyAddressBook")
address_book.add_contact(contact)


# Displaying the contact details
print("\n--------------Contact Details:---------------")
print(contact.display_contact())
