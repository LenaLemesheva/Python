import view


def log_to_file(contact):

    with open('row.csv', 'a', encoding='UTF-8') as file:
        file.write(
            f'{contact[0]}; {contact[1]}; {contact[2]}; {contact[3]}; {contact[4]};\n')

    with open('column.csv', 'a', encoding='UTF-8') as file:
        file.write(
            f'{contact[0]}\n {contact[1]}\n {contact[2]}\n {contact[3]} {contact[4]}\n\n\n')

