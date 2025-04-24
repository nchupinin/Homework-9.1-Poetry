from typing import Any, Dict, List

from src.processing import filter_by_state, sort_by_date
from src.masks import get_mask_card_number
from src.widget import get_date, get_mask_account


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


if __name__ == "__main__":
    main()
