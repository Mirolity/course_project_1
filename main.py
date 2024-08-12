import json
from datetime import datetime


def load_operations(file_path):
    """Загрузить операции из JSON файла."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def mask_card(card_number):
    """Замаскировать номер карты."""
    return f"{card_number[:6]} {card_number[6:8]}** **** {card_number[-4:]}"


def mask_account(account_number):
    """Замаскировать номер счета."""
    return f"**{account_number[-4:]}"


def format_operation(operation):
    """Форматировать операцию для вывода."""
    date = datetime.fromisoformat(operation['date'][:-1]).strftime('%d.%m.%Y')
    description = operation.get('description', 'Нет описания')

    from_ = mask_card(operation['from']) if 'from' in operation else None
    to_ = mask_account(operation['to'])

    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']

    formatted_operation = f"{date} {description}\\n"
    formatted_operation += f"{from_} -> {to_}\\n"
    formatted_operation += f"{amount} {currency}"

    return formatted_operation


def display_last_operations(operations, count=5):
    """Вывести последние успешные операции."""
    executed_operations = [op for op in operations if op['state'] == 'EXECUTED']
    executed_operations.sort(key=lambda x: x['date'], reverse=True)

    for operation in executed_operations[:count]:
        print(format_operation(operation))
        print()  # Пустая строка для разделения операций


if __name__ == "__main__":
    operations = load_operations('data/operations.json')
    display_last_operations(operations)
