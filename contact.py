from termcolor import colored


def add_contact(contacts: list[dict]):
    
    while True:
            first_name = input(colored("Ism: ", "yellow"))
            if not first_name.isalpha():
                print(colored("Xato ism", "red"))
            else:
                break

    while True:
        last_name = input(colored("Familya (majburiy emas): ", "yellow"))
        if last_name == "" or last_name.isalpha():
            break
        else:
            print(colored("Xato! Familya faqat harflardan iborat bo'lishi shart\n(yoki: shunchaki 'ENTER'ni bosib ketsangi ham bo'ladi)", "red"))

    while True:
        phone = input(colored("Raqam: ", "yellow"))
        if not phone.isdigit():
            print(colored("Siz raqam kitishingiz kerak", "red"))
        else:
            break
    while True:

        group = input(colored("== Guruh tanlang ==\n1. Oila\n2. Do'stlar\n3. Ish\n4. Boshqalar\n", "yellow"))

        if group == "1":
            group = "Oila"
            break
        elif group == "2":
            group = "Do'stlar"
            break
        elif group == "3":
            group = "Ish"
            break
        elif group == "4":
            group = "Boshqalar"
            break
        else:
            print(colored("Xato tanlov", "red"))
            
    contacts.append({
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "group": group,
    })
    print(colored("Kontakt qo'shildi!\n", "green"))



def show_all_contact(contacts: list[dict]):

    if not contacts:
            print(colored("Kontaktlar yo'q\n", "red"))

    for i, contact in enumerate(contacts):
        print(f"{i+1}. {contact['first_name']} {contact['last_name']} | +{contact['phone']} | {contact['group']}")



def search_contact(contacts: list[dict]):
   
    search_name = input("Qidirilayotgan kontakt (nomi, familyasi, raqami): ").strip().lower()
    found = False
    for contact in contacts:
        if contact['first_name'].lower() == search_name or contact['last_name'].lower() == search_name or contact['phone'].lower() == search_name:
            print("Topildi:", contact['first_name'], contact['last_name'], "|", contact['phone'], "|", contact['group'], "\n")
            found = True
            break
    if not found:
        print(colored("Kontakt topilmadi.\n", "red"))



def delete_contact(contacts: list[dict]):
    delete_name = input("O'chirmoqchi bo'lgan kontakt (nomi, familyasi, raqami): ").strip().lower()
    for contact in contacts:
        if contact['first_name'].lower() == delete_name or contact['last_name'].lower() == delete_name or contact['phone'].lower() == delete_name:
            contacts.remove(contact)
            print(colored("Kontakt o'chirildi!\n", 'green'))
        else:
            print(colored("Bunday kontakt topilmadi.\n", "red"))



def update_contact(contacts: list[dict]):
    update_name = input("Yangilamoqchi bo'lgan kontakt ismi: ").strip().lower()
    found = False

    for contact in contacts:
        if contact['first_name'].lower() == update_name:
            print(colored("Hozirgi ma'lumotlar:", "yellow"),
                    f"{contact['first_name']} {contact['last_name']} | {contact['phone']} | {contact['group']}")

            # Ism
            while True:
                new_first_name = input(f"Yangi ism ({contact['first_name']}): ")
                if new_first_name == "":
                    new_first_name = contact['first_name']
                    break
                elif not new_first_name.isalpha():
                    print(colored("Xato ism!", "red"))
                else:
                    break

            # Familya
            while True:
                new_last_name = input(f"Yangi familya ({contact['last_name']}): ")
                if new_last_name == "":
                    new_last_name = contact['last_name']
                    break
                elif not new_last_name.isalpha():
                    print(colored("Xato familya!", "red"))
                else:
                    break

            # Telefon
            while True:
                new_phone = input(f"Yangi raqam ({contact['phone']}): ")
                if new_phone == "":
                    new_phone = contact['phone']
                    break
                elif not new_phone.isdigit():
                    print(colored("Faqat raqam kiriting!", "red"))
                else:
                    break

            # Guruh
            while True:
                group_input = input(colored("== Yangi guruh tanlang ==\n1. Oila\n2. Do'stlar\n3. Ish\n4. Boshqalar\n", "yellow"))
                if group_input == "":
                    new_group = contact['group']
                    break
                elif group_input == "1":
                    new_group = "Oila"
                    break
                elif group_input == "2":
                    new_group = "Do'stlar"
                    break
                elif group_input == "3":
                    new_group = "Ish"
                    break
                elif group_input == "4":
                    new_group = "Boshqalar"
                    break
                else:
                    print(colored("Xato tanlov", "red"))

            # Yangisi
            contact['first_name'] = new_first_name
            contact['last_name'] = new_last_name
            contact['phone'] = new_phone
            contact['group'] = new_group

            print(colored("Kontakt muvaffaqiyatli yangilandi!\n", "green"))
            found = True
            break

    if not found:
        print(colored("Kontakt topilmadi.\n", "red"))


    
def contact_groups(contacts: list[dict]):
    group_name = input("Qaysi guruhni ko'rsatmoqchisiz? (Oila, Do'stlar, Ish, Boshqalar): ").strip().lower()
    found = False
    for contact in contacts:
        if contact['group'].strip().lower() == group_name:
            print(f"{contact['first_name']} {contact['last_name']} | +{contact['phone']} | {contact['group']}")
            found = True
    if not found:
        print(colored("Bunaqa guruh mavjud emas\n", "red"))



def print_menu():
    colored_menu_text = colored("""
========= Menu =========
1. Add Contact 
2. Show Contacts
3. Search Contact
4. Delete Contact
5. Update Contact
6. Grouped Contacts
7. Exit
""", "green")

    print(colored_menu_text)
