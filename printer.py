from termcolor import colored


def print_menu():
    colored_menu_text = colored("""
    ========= Menu =========
    1. Add Contact 
    2. Show Contacts
    3. Search Contact
    4. Delete Contact
    5. Update Contact
    6. Exit
    """, "green")

    print(colored_menu_text)


def print_status(status: str):
    status_data = {
        'error': colored("xatolik yuz berdi", 'red'),
        'success': colored("muvaffasiyatli bajarildi", 'green'),
    }

    print(status_data[status])


def print_contact(contact: dict):
    print(f"{contact['first_name']} {contact['last_name']}, {contact['phone']}, {contact['group']}")


def print_all_contact(contacts: list[dict]):
    print("ALl Contacts")
    for contact in contacts:
        print_contact(contact)

