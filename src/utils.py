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
