import sys


def close_command():
    print('Good bye!')
    sys.exit(1)


def hello_command():
    print('How can I help you?')


def add_contact_command(args: list, contacts: dict):
    name, phone = args
    contacts[name] = phone
    print('Contact added.')


def change_contact_command(args: list, contacts: dict):
    name, phone = args
    contacts[name] = phone
    print('Contact changed.')


def get_contact_command(args: list, contacts: dict):
    name = args[0]
    print(contacts.get(name, 'Contact not found.'))


def get_contacts_command(contacts: dict):
    print(contacts)
