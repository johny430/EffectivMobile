import csv

data = []


def read_data():
    with open('data.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data


def write_data(data):
    with open('data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Дата', 'Категория', 'Сумма', 'Описание']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def show_balance(data):
    total_income = sum(int(row['Сумма']) for row in data if row['Категория'] == 'Доход')
    total_expense = sum(int(row['Сумма']) for row in data if row['Категория'] == 'Расход')
    balance = total_income - total_expense
    print(f"Текущий баланс: {balance}")
    print(f"Сумма доходов: {total_income}")
    print(f"Сумма расходов: {total_expense}")


def add_record():
    date = input("Введите дату (гггг-мм-дд): ")
    category = input("Введите категорию (Доход/Расход): ")
    amount = input("Введите сумму: ")
    description = input("Введите описание: ")
    new_record = {'Дата': date, 'Категория': category, 'Сумма': amount, 'Описание': description}
    data.append(new_record)
    write_data(data)
    print("Запись успешно добавлена")


def edit_record():
    date_to_edit = input("Введите дату записи для редактирования (гггг-мм-дд): ")
    for row in data:
        if row['Дата'] == date_to_edit:
            print("Найдена запись для редактирования:")
            print(f"Дата: {row['Дата']}, Категория: {row['Категория']}, Сумма: {row['Сумма']}, Описание: {row['Описание']}")
            choice = input("Что вы хотите отредактировать (Дата/Категория/Сумма/Описание)? Введите '0' для выхода: ")
            if choice == '0':
                break
            new_value = input(f"Введите новое значение для {choice}: ")
            row[choice] = new_value
            write_data(data)
            print("Запись успешно отредактирована")
            break
    else:
        print("Запись с указанной датой не найдена")


def search_record():
    search_criteria = input("Введите критерий поиска (Дата/Категория/Сумма): ")
    search_value = input(f"Введите значение для критерия {search_criteria}: ")

    matching_records = [row for row in data if row.get(search_criteria) == search_value]

    if matching_records:
        print("Найденные записи:")
        for record in matching_records:
            print(f"Дата: {record['Дата']}, Категория: {record['Категория']}, Сумма: {record['Сумма']}, Описание: {record['Описание']}")
    else:
        print("Нет записей, удовлетворяющих критериям поиска")


data = read_data()

while True:
    print("\nВыберите действие:")
    print("1. Показать баланс")
    print("2. Добавить запись")
    print("3. Редактировать запись")
    print("4. Поиск по записям")
    print("0. Выйти")

    choice = input("Введите номер действия: ")

    if choice == '1':
        show_balance(data)
    elif choice == '2':
        add_record()
    elif choice == '3':
        edit_record()
    elif choice == '4':
        search_record()
    elif choice == '0':
        print('Завершение работы')
        break
