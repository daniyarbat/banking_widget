from utils import get_data, get_filtered_data, get_last_operations, get_format_date, get_card_number, get_account_number, file_path


def main():
    data = get_data(file_path)
    filtered_data = get_filtered_data(data)
    last_operations = get_last_operations(filtered_data)


if __name__ == '__main__':
    main()
