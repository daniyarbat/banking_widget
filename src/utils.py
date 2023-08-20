import json
import os
from datetime import datetime

# Получение пути к текущей директории
current_directory = os.path.dirname(os.path.abspath(__file__))

# Составление полного пути к файлу operations.json
file_path = os.path.join(current_directory, '..', 'data', 'operations.json')

def get_data(file_path):
    with open(file_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


# Фильтрация данных с нужным ключом
def get_filtered_data(data):
    filtered_data = []
    for x in data:
        if 'state' in x and x['state'] == 'EXECUTED':
            filtered_data.append(x)
    return filtered_data


# форматирование номера карты
def get_card_number(card_info):
    #return card_number[:4] + ' ' + card_number[4:6] + '**' + ' ' + '****' + ' ' + card_number[-4:]
    #digits = ''.join(filter(str.isdigit, card_number))
    # Маскируем номер карты
    #masked_number = digits[:4] + ' ' + digits[4:6] + '** **** ' + digits[-4:]
    #return masked_number

    card_name, card_number = card_info.split(' ', 1)

    # Получаем только цифры из номера карты
    digits = ''.join(filter(str.isdigit, card_number))

    # Маскируем номер карты
    masked_number = digits[:4] + ' ' + digits[4:6] + '** **** ' + digits[-4:]

    return f"{card_name} {masked_number}"

# Форматирование номера счета
def get_account_number(account_info):
    account_name, account_number = account_info.split(' ', 1)

    digits = ''.join(filter(str.isdigit, account_number))
    masked_num = '**' + digits[-4:]
    return f"{account_name} {masked_num}"


# Получение даты в нужном формате
def get_format_date(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
    return date.strftime('%d.%m.%Y')


# Получение последних 5 операций из списка
def get_last_operations(data):
    def get_date(item):
        return item['date']

    data = sorted(data, key=get_date, reverse=True)
    return data[:5]
