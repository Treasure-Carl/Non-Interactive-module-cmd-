import cmd

# CRUDE - Creat Read Update Delete Exit

class AddressBook(cmd.Cmd):
    intro = "welcome to my Address Book. Type 'help' for commands. \n"
    prompt = "(Address Book)> "

    def __init__(self):
        super().__init__()
        self.contacts = {}

    def do_add(self, args):
        """Add a new contact to the address book. Usage <phone> <name>"""
        phone, name = args.split()
        if phone not in self.contacts:
            self.contacts[phone] = name
            print(f"Contact added {phone} - {name}")

        else:
            print("Contact {phone} already exists. Use update <phone> <name> to update contact")

    def do_read(self, args):
        """Reads all contacts"""
        if not self.contacts:
            print("No contacts found.")

        else:
            for phone, name in self.contacts.items():
                print(f"{phone} - {name}")

    def do_update(self, args):
        """Update a contacts. Usage: update <phone> <new_name>"""
        phone, new_name = args.split()
        if phone in self.contacts:
            self.contacts[phone] = new_name
            print(f"Contacts  name updated: {phone} - {new_name}")
        else:
            print(f"{phone} not in contacts")

    def do_delete(self, args):
        """Delete selected contacts from Address Phonebook. Usage: delete <phone> <name>"""
        phone, name = args.split()
        if phone in self.contacts and self.contacts[phone] == name:
            del self.contacts[phone]
            print(f"{name} - {phone} successfully deleted")
        else:
            print("Contact not found or name does not match the provided phone number.")

    def do_exit(self, args):
        """"Exits our Address Book"""
        return True

if __name__ == "__main__":
    AddressBook().cmdloop()