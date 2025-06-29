import time
from sys import exit
from termcolor import colored
from contact import add_contact, show_all_contact, search_contact, delete_contact, update_contact, contact_groups, print_menu



def main():
    contacts: list[dict] = [
        {'first_name': 'Ali', 'last_name': 'Valiyev', 'phone': '998993108382', "group": "Do'stlar"},
        {"first_name": 'Parviz', 'last_name': 'Boltayev', 'phone': '99899777777', "group": "Do'stlar"},
        {"first_name": 'Mom', 'last_name': '', 'phone': '998951111111', "group": 'Oila'}
    ]
    
    while True:
        print_menu()

        choice = input("Menu tanlang: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            show_all_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            update_contact(contacts)
        elif choice == '6':
            contact_groups(contacts)
        elif choice == '7':
            print(colored("Dasturdan chiqilmoqda...", "yellow"))
            time.sleep(2)
            print(colored("Siz dasturdan chiqdingiz", "green"))
            exit(0)
        else:
            print(colored("Noto'g'ri tanlov. Qaytadan urinib ko'ring.\n", "red"))

if __name__ == "__main__":
    main()
