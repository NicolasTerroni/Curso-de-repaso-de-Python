from contact_mod import Contact
import csv

class ContactBook:
    def __init__(self):
        self._contacts = []
    
    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()
        
    def update_contact(self):
        update_position = int(input("Wich position do yo want to update? ---> "))-1
        self._contacts.pop(update_position)
        name = input("New name: ")
        phone = input("New phone: ")
        email = input("New Email: ")
        new_contact = Contact(name, phone, email)
        self._contacts.insert(update_position,new_contact)
        self._save()

    def search_contact(self):
        name_search = input("What contact do yo want to see? (name) ---> ")
        for contact in self._contacts:
            if name_search == contact.name:
                print("------------------------------------------------")
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                print("------------------------------------------------")
                break
        else:
            print("There's no result.")

    def delete_contact(self):
        delete = int(input("What position do you want to delete? ---> "))-1
        self._contacts.pop(delete)
        self._save()

    def show_contacts(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def _print_contact(self, contact):
        print("------------------------------------------------")
        print(f"Name: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print("------------------------------------------------")

    def _save(self):
        with open ("contacts.csv","w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow( ("Name","Phone","Email") )

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )
    