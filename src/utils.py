import json
from datetime import datetime


# Чтение данных из файла operations.json
def get_data():
    with open('data/operations.json', 'r', encoding='UTF-8') as file:
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
def get_card_number(card_number):
    if len(card_number) != 16:
        return "Неверный номер карты"
    return card_number[:4] + ' ' + card_number[4:6] + '**' + ' ' + '****' + ' ' + card_number[-4:]


# Форматирование номера счета
def get_account_number(account_number):
    if len(account_number) != 20:
        return "Неверный номер счета"
    return '**' + account_number[-4:]



