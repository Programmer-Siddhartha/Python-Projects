# Initialize an empty contact book
contact_book = {}

# Function to add a contact
def add_contact():
    name = input("Enter the contact name: ").strip().lower()  # Convert to lowercase
    phone = input("Enter the phone number: ").strip()
    contact_book[name] = phone
    print(f"Contact '{name.title()}' added.")  # Display the name with the first letter capitalized

# Function to remove a contact
def remove_contact():
    name = input("Enter the contact name to remove: ").strip().lower()  # Convert to lowercase
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name.title()}' removed.")  # Display the name with the first letter capitalized
    else:
        print("Contact not found.")

# Function to search for a contact
def search_contact():
    name = input("Enter the contact name to search: ").strip().lower()  # Convert to lowercase
    if name in contact_book:
        print(f"{name.title()}'s phone number is {contact_book[name]}")  # Display the name with the first letter capitalized
    else:
        print("Contact not found.")

# Function to display all contacts
def display_contacts():
    if contact_book:
        print("Contact Book:")
        for name, phone in contact_book.items():
            print(f"{name.title()}: {phone}")  # Display each name with the first letter capitalized
    else:
        print("No contacts in the contact book.")

# Main function to run the contact book program
def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            remove_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            display_contacts()
        elif choice == "5":
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the contact book program
main()
