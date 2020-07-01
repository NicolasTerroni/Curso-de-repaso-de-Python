# Agenda de contactos, un agrupador de contactos que nos permita añadir eliminar y ver contactos
from contact_mod import Contact
from contact_book_mod import ContactBook
import csv

def run():
    
    contact_book = ContactBook()

    with open("contacts.csv", "r") as file:
        reader = csv.reader(file)
        for i , row in enumerate(reader):
            if i == 0:
                continue
            elif row == []:
                continue
            else:
                contact_book.add_contact( row[0], row[1], row[2] )

    while True:
        command = input("""Select an option:
        1) Add contact
        2) Update contact
        3) Search contact
        4) Delete contact
        5) Show contacts
        6) Exit
        
        -----> """)

        if command == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            contact_book.add_contact(name, phone, email)        
        elif command == "2":
            contact_book.update_contact()
        elif command == "3":
            contact_book.search_contact()
        elif command == "4":
            contact_book.delete_contact()
        elif command == "5":
            contact_book.show_contacts()
        elif command == "6":
            return False
        else:
            print("Command does not exist.")

if __name__ == "__main__":
    print("~ C O N T A C T    B O O K ~")
    run()