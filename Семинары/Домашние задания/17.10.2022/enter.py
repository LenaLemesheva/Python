
def enter():
    contact = []
    sirname = input('Введите фамилию: ')
    contact.append(sirname.title())
    name = input('Введите имя: ')
    contact.append(name.title())
    patronymic = input('Введите отчество: ')
    contact.append(patronymic.title())
    phone_number = input('Введите номер телефона: ')
    contact.append(phone_number)
    any_info = input('Описание: ')
    contact.append(any_info.title())
    print('Абонент записан: ', contact)
    return contact