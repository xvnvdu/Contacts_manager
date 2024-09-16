import json
import re


class ContactManager:
    def __init__(self):
        try:
            with open('contacts.txt', 'r') as file:
                self.contacts = json.load(file)
        except (FileNotFoundError, ValueError):
            self.contacts = []

    def add_contact(self, name, phone, email):
        contact = {'name': name, 'phone': phone, 'email': email}
        self.contacts.append(contact)
        self.save_contacts()

    @staticmethod
    def validate_phone(phone):
        pattern = r'^\+\d{7,15}$'
        if bool(re.match(pattern, phone)):
            return True
        else:
            print('Номер телефона указан некорректно! (Начинайте ввод с "+")')
            return False

    @staticmethod
    def validate_email(email):
        pattern = r'^(?!\.)[a-zA-Z0-9._-]+(?<!\.)@[a-zA-Z]+\.[a-zA-Z]+$'
        if bool(re.match(pattern, email)):
            return True
        else:
            print('Почта указана некорректно!')
            return False

    def find_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact['name'].lower():
                found_contacts.append(contact)
        return found_contacts if found_contacts else None

    def delete_contact(self, contact):
        if contact:
            while True:
                try:
                    choice = int(input('| Да - 0 | Нет - 1 |: '))
                except ValueError:
                    print('Вам нужно ввести число (0 или 1)!')
                    continue
                if choice == 0:
                    self.contacts.remove(contact)
                    print('Контакт успешно удален !')
                    break
                elif choice == 1:
                    break
                else:
                    print('Вам нужно ввести число (0 или 1)!')
                    space()
            self.save_contacts()

    def display_contacts(self, contacts_list=None):
        if contacts_list is None:
            contacts_list = self.contacts
        for contact in contacts_list:
            print(f"Name: {contact['name']}, "
                  f"Phone: {contact['phone']}, "
                  f"Email: {contact['email']} \n")

    def save_contacts(self):
        with open('contacts.txt', 'w') as file:
            json.dump(self.contacts, file, indent=4)


class Contact:
    def __init__(self, name='', phone='', email=''):
        self.name = name
        self.phone = phone
        self.email = email

    def update_name(self, name):
        self.name = name

    def update_phone(self, phone):
        self.phone = phone

    def update_email(self, email):
        self.email = email

    def update_all(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


contact_manager = ContactManager()
class_contact = Contact()

while True:
    command = input('Введите команду (add, find, delete, show, sort, edit, exit): ').lower()

    def space():
        print('')
    space()

    if command == 'add':
        name = input('Введите имя: ')
        while True:
            phone = input('Введите телефон: ')
            if ContactManager.validate_phone(phone):
                break
            else:
                continue
        while True:
            email = input('Введите почту: ')
            if ContactManager.validate_email(email):
                break
            else:
                continue
        contact_manager.add_contact(name, phone, email)
        print('\nКонтакт успешно сохранен !')

    elif command == 'find':
        name = input('Введите имя: ')
        space()
        contacts_found = contact_manager.find_contact(name)
        if contacts_found:
            for contact in contacts_found:
                print(f"Name: {contact['name']}, "
                      f"Phone: {contact['phone']}, "
                      f"Email: {contact['email']} \n")
            space()
        else:
            print('Контакт не найден')
            space()

    elif command == 'delete':
        name = input('Введите имя контакта, который хотите удалить: ')
        contact_list = contact_manager.find_contact(name)
        if contact_list:
            if len(contact_list) > 1:
                print('Найдены следующие контакты:\n')
                num_in_list = 1
                for contact in contact_list:
                    print(f"{num_in_list}) Name: {contact['name']}, "
                          f"Phone: {contact['phone']}, "
                          f"Email: {contact['email']} \n")
                    num_in_list += 1
                while True:
                    try:
                        num_change = int(input('\nВведите номер контакта, который хотите удалить: '))
                        space()
                    except:
                        space()
                        print('Вам нужно ввести целое число!')
                        continue
                    if 0 < num_change <= len(contact_list):
                        contact = contact_list[num_change - 1]
                        print('Удалить контакт?:')
                        print(f"Name: {contact['name']}, "
                              f"Phone: {contact['phone']}, "
                              f"Email: {contact['email']} \n")
                        contact_manager.delete_contact(contact)
                        break
                    else:
                        print('Вам нужно выбрать номер из списка!')
            else:
                print('\nНайден единственный контакт:')
                for contact in contact_list:
                    print(f"Name: {contact['name']}, "
                          f"Phone: {contact['phone']}, "
                          f"Email: {contact['email']} \n")
                    print('Удалить контакт?')
                    contact_manager.delete_contact(contact)
        else:
            print('\nКонтакт не найден')
            space()
            continue
        space()

    elif command == 'edit':
        contact_manager.display_contacts()
        space()

        while True:
            name = input('Введите имя контакта, который хотите изменить: ')
            space()
            contact_list = contact_manager.find_contact(name)

            if contact_list:
                if len(contact_list) > 1:
                    print('Найдены следующие контакты:\n')
                    num_in_list = 1
                    for contact in contact_list:
                        print(f"{num_in_list}) Name: {contact['name']}, "
                              f"Phone: {contact['phone']}, "
                              f"Email: {contact['email']} \n")
                        num_in_list += 1
                    while True:
                        try:
                            num_change = int(input('\nВведите номер контакта, который хотите изменить: '))
                            space()
                        except:
                            print('Вам нужно ввести целое число!')
                            continue
                        if 0 < num_change <= len(contact_list):
                            contact = contact_list[num_change-1]
                            print('Изменяемый контакт:')
                            print(f"{num_in_list}) Name: {contact['name']}, "
                                  f"Phone: {contact['phone']}, "
                                  f"Email: {contact['email']} \n")
                            break
                        else:
                            print('Вам нужно выбрать номер из списка!')
                else:
                    print('Найден единственный контакт:')
                    for contact in contact_list:
                        print(f"Name: {contact['name']}, "
                              f"Phone: {contact['phone']}, "
                              f"Email: {contact['email']} \n")

                current_contact = Contact(contact['name'], contact['phone'], contact['email'])
                while True:
    edit_choice = input('Введите команду, чтобы изменить контакт:\n'
                        'Изменить имя - name\n'
                        'Изменить телефон - phone\n'
                        'Изменить почту - email\n'
                        'Изменить контакт полностью - all\n').lower()
                    if edit_choice == 'name':
                        name = input('Введите имя контакта: ')
                        space()
                        print('Имя успешно изменено !\n')
                        current_contact.update_name(name)
                        break
                    elif edit_choice == 'phone':
                        while True:
                            phone = input('Введите телефон контакта: ')
                            if ContactManager.validate_phone(phone):
                                break
                            else:
                                continue
                        space()
                        print('Телефон успешно изменен !\n')
                        current_contact.update_phone(phone)
                        break
                    elif edit_choice == 'email':
                        while True:
                            email = input('Введите почту контакта: ')
                            if ContactManager.validate_email(email):
                                break
                            else:
                                continue
                        print('Почта успешно изменена !\n')
                        current_contact.update_email(email)
                        break
                    elif edit_choice == 'all':
                        name = input('Введите имя контакта: ')
                        while True:
                            phone = input('Введите телефон контакта: ')
                            if ContactManager.validate_phone(phone):
                                break
                            else:
                                continue
                        while True:
                            email = input('Введите почту контакта: ')
                            if ContactManager.validate_email(email):
                                break
                            else:
                                continue
                        space()
                        print('Контакт успешно изменен !')
                        current_contact.update_all(name, phone, email)
                        break
                    else:
                        space()
                        print('Вам нужно ввести команду из списка ниже!\n')
                        continue

                contact['name'] = current_contact.name
                contact['phone'] = current_contact.phone
                contact['email'] = current_contact.email

                contact_manager.save_contacts()
                break

            else:
                print('Контакт не найден')
                space()

    elif command == 'show':
        contact_manager.display_contacts()
        space()

    elif command == 'sort':
        while True:
            try:
                choise = int(input('Введите число\n0 - A-Z\n1 - Z-A\n'))
                space()
            except ValueError:
                print('Вам нужно ввести число (0 или 1)!')
                continue

            if choise == 0:
                sorted_contacts = sorted(contact_manager.contacts, key=lambda contact: contact['name'])
                contact_manager.display_contacts(sorted_contacts)
                space()
                break
            elif choise == 1:
                sorted_contacts = sorted(contact_manager.contacts, key=lambda contact: contact['name'], reverse=True)
                contact_manager.display_contacts(sorted_contacts)
                space()
                break
            else:
                print('Вам нужно ввести число (0 или 1)!')
                continue

    elif command == 'exit':
        break

    else:
        print('Введите команду из списка')
        space()
