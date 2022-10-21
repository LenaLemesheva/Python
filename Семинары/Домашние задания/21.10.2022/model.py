import csv


def csv_data_open():      # 1 - импорт csv
    with open("Семинары/Домашние задания/21.10.2022/csv_data.csv", encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=";")
        res = list(file_csv)
    return res


def add_info(list):  # 2- добавление информации
    with open("Семинары/Домашние задания/21.10.2022/csv_data.csv", "a", encoding="utf8", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(list)


def del_info(index):  # удаление информации
    list_csv = csv_data_open()
    print(list_csv)
    del list_csv[index]
    with open("Семинары/Домашние задания/21.10.2022/csv_data.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)

            
def update_info(index, tel):  # обнавление информации
    list_csv = csv_data_open()
    list_csv[index][3] = tel
    with open("Семинары/Домашние задания/21.10.2022/csv_data.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)


def export_csv():     # экспорт csv
    with open('Семинары/Домашние задания/21.10.2022/csv_data.csv', encoding="utf8") as csvfile, open('Семинары/Домашние задания/21.10.2022/csv_data_out.csv', 'w', encoding="utf8", newline='') as f:
        reader = csv.reader(csvfile, delimiter=';')
        writer = csv.writer(f, delimiter=';')
        for row in reader:
            writer.writerow(row)