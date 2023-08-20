from utils import get_data, get_filtered_data, get_last_operations, get_format_date, get_card_number,\
    get_account_number, file_path


# Основной код программы
def main():
    data = get_data(file_path)
    filtered_data = get_filtered_data(data)
    last_operations = get_last_operations(filtered_data)

    for operation in last_operations:
        date = get_format_date(operation['date'])
        description = operation['description']
        from_account = operation.get('from', '')
        to_account = operation['to']
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        if from_account.startswith("Счет"):
            from_account = get_account_number(from_account)
        elif from_account.startswith("Visa") or from_account.startswith("MasterCard") or \
                from_account.startswith("Maestro") or from_account.startswith("МИР"):
            from_account = get_card_number(from_account)

        to_account = get_account_number(to_account)

        print(f'{date} {description}')
        print(f'{from_account} -> {to_account}')
        print(f'{amount} {currency}\n')


if __name__ == '__main__':
    main()
