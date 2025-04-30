from typing import Any, Dict, List

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def main() -> None:
    """Основная функция для демонстрации работы модулей"""

    # Демонстрация работы с картами и счетами
    card_number: str = "7080792289066543"
    print("Маскированный номер карты:", get_mask_card_number(card_number))

    account_number: str = "1234567890123456"
    print("Маскированный номер счета:", get_mask_account(account_number))

    transaction_date: str = "2024-03-11T02:26:18.671407"
    print("Дата банковской операции:", get_date(transaction_date))

    # Подготовка тестовых данных
    transactions: List[Dict[str, Any]] = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    # Фильтрация выполненных операций
    executed_transactions: List[Dict[str, Any]] = filter_by_state(transactions, "EXECUTED")
    print("\nВыполненные операции:")
    for transaction in executed_transactions:
        print(f"{transaction['date']} - {transaction['id']}")

    # Сортировка всех операций по дате
    sorted_transactions: List[Dict[str, Any]] = sort_by_date(transactions)
    print("\nВсе операции, отсортированные по дате:")
    for transaction in sorted_transactions:
        print(f"{transaction['date']} - {transaction['id']}")

    print()
    print(mask_account_card("Счет 12345678901234567890"))  # Счет **7890
    print(mask_account_card("Visa 1234567890123456"), end="\n")  # Visa 1234 56** **** 3456
    print()

    number = card_number_generator()
    print(next(number))
    print(next(number))
    print(next(number))
    print(next(number))
    print(next(number))
    print()

    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    print(next(filter_by_currency(transactions, "USD")))
    print(next(transaction_descriptions(transactions)))
    print(next(transaction_descriptions(transactions)))
    print(next(transaction_descriptions(transactions)))


if __name__ == "__main__":
    main()
