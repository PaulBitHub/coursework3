import sys
from datetime import datetime

def find_executed_elements(list_data):
    """Находит по ключу 'state' executed операции и вносит их в лист"""
    if not isinstance(list_data, list):
        print("Проверьте вводные данные - они должны быть формата list")
        sys.exit(1)

    executed_list = []
    for operation in list_data:
        try:
            if 'state' in operation and operation['state'] == 'EXECUTED':
                executed_list.append(operation)
        except KeyError:
            continue

    return executed_list

def format_date(date):
    """Преобразует дату из 2019-08-26T10:50:58.294041 в дд.мм.гггг"""
    if not isinstance(date, str):
        print("Проверьте вводные данные - они должны быть формата string")
        sys.exit(1)
    date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date

def format_secret_card(data_str):
    """Принимает строку. Если содержит 'Счет' - маскирует по типу **1234
    Если НЕ СЧЕТ - 1234 56** **** 7890"""
    list_for_check = ['Счет', 'Счёт', 'счет', 'счёт']
    start_words = data_str[:len(data_str) - 16]
    for_mask_part = data_str[-16:]
    if any(substring in data_str for substring in list_for_check):
        start_words = data_str[:len(data_str) - 20]
        mask_part = '**' + for_mask_part[-4:]
    else:
        mask_part = for_mask_part[:4] + ' ' + for_mask_part[4:6] + '** **** ' + for_mask_part[-4:]

    return start_words + mask_part

def date_to_int(date_str):
    """Строку даты с ':' 'T' '-' возвращает в виде числа"""
    modified_string = date_str.replace(":", "").replace("T", "").replace("-", "").replace(".", "")
    return int(modified_string)

def display_transaction(ready_data):
    """Читает лист и выводит данные в удобном формате для пользователя
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>"""
    if not isinstance(ready_data, list):
        print("Проверьте вводные данные - они должны быть формата list")
        sys.exit(1)
    for operation in ready_data:
        try:
            block = (f'{format_date(operation["date"])} {operation["description"]}\n'
                     f'{format_secret_card(operation["from"])} -> {format_secret_card(operation["to"])}\n'
                     f'{operation['operationAmount']["amount"]} {operation['operationAmount']["currency"]['name']}\n'
                     f'')
        except KeyError:
            block = (f'{format_date(operation["date"])} {operation["description"]}\n'
                     f'Использован {format_secret_card(operation["to"])}\n'
                     f'{operation['operationAmount']["amount"]} {operation['operationAmount']["currency"]['name']}\n'
                     f'')
        print(block)
