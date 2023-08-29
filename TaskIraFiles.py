# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

phone_book = {}
PATH = 'Phones.txt'


def open_file(book: list):
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()       
    for i, contact in enumerate(data, 1):
        contact = contact.strip().split(';')
        book[i] = contact


def save_file(book: dict):
    all_contacts = []
    for contact in book.values():
        all_contacts.append(';'.join(contact))
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(all_contacts))


def show_all_contacts(book: dict, message: str):
    print('\n' + '=' * 68)
    if book:
        for i, contact in book.items(): 
            print(f'{i:>3}.  {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}')
    else:
        print(message)
    print('=' * 68 + '\n')


def find_contact(book: list, search: str):
    result = {}
    for i, contact in book.items():
        for field in contact:
            if search.lower() in field.lower():
                result[i] = contact
                break
    return result


def func_search(book: dict):
    search = input('Что будем искать? -> ')
    result = find_contact(book, search)
    show_all_contacts(result, f'Контакт содержащий {search} не найден!')


def add_new_contact(book: dict, new: list):
    cur_id = max(book.keys()) + 1
    book[cur_id] = new


def change_contact(book: dict, cid: int):
    name, phone, comment = book.get(cid)
    changed = []
    for item in ['Введите новое имя (или оставте пустым, чтоб не изменять): \n --> ',
                 'Введите новый телефон (или оставте пустым, чтоб не изменять): \n --> ',
                 'Введите новый комментарий (или оставте пустым, чтоб не изменять): \n --> ']:
        changed.append(input(item))
    book[cid] = [changed[0] if changed[0] else name, changed[1] if changed[1] else phone, changed[2] if changed[2] else comment]
    return changed[0] if changed[0] else name


def delete_contact(book: dict, cid: int):
    name = book.pop(cid)
    return name[0]
    

def menu():
    print()
    menu_points = ['Открыть файл', 
                   'Сохранить файл', 
                   'Посмотреть все контакты', 
                   'Найти контакт', 
                   'Добавить контакт', 
                   'Изменить контакт', 
                   'Удалить контакт', 
                   'Выход']
    print('Главное меню')
    [print(f'\t{i}. {item}') for i, item in enumerate(menu_points, 1) ]
    choice = int(input('Выберите пункт меню: '))
    print()
    return choice


while True:
    choice = menu()
    match choice:

        case 1:
            open_file(phone_book)
            print('\n Телефонная книга успешно открыта!\n')

        case 2:
            save_file(phone_book)
            print('\n Телефонная книга успешно сохранена!\n')

        case 3:
            show_all_contacts(phone_book, 'Телефонная книга пуста или не открыта.')
        
        case 4:
            func_search(phone_book)

        case 5:
            new = []
            for item in ['Введите имя: ', 'Введите телефон: ', 'Введите коммент: ']:
                new.append(input(item))
            add_new_contact(phone_book, new)
            print(f'\n Контакт {new[0]} успешно добавлен!\n')
        
        case 6:
            func_search(phone_book)
            select = int(input('Какой контакт будем именять? '))
            name = change_contact(phone_book, select)
            print(f'\n Контакт {name} успешно изменен!\n')
        
        case 7:
            func_search(phone_book)
            select = int(input('Какой контакт будем удалять? '))
            name = delete_contact(phone_book, select)
            print(f'\n Контакт {name} успешно удален! \n')
        
        case 8:
            print('Всего хорошего!')
            break
