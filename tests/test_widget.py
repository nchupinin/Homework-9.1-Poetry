from typing import Union

import pytest

from main import get_date, mask_account_card


@pytest.mark.parametrize(
    "valid_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-10-18T01:11:12.123456", "18.10.2025"),
        ("2022-01-21T05:05:10.765432", "21.01.2022"),
    ],
)
def test_valid_get_data(valid_date: str, expected: str) -> None:
    """Тест проверки входящих валидных данных даты"""
    assert get_date(valid_date) == expected


@pytest.mark.parametrize(
    "invalid_date",
    [
        "2025.10.18T01:11:12.123456",  # Неправильный разделитель (должен быть '-')
        "2022-13-21T05:05:10.765432",  # Количество месяцев не может превышать 12
        "2022-01-32T05:05:10.765432",  # Количество дней не может превышать 31
        "",  # Пустая строка
        None,  # "Дата не может быть None"
        123456789,  # "Входные данные должны быть строкой"
    ],
)
def test_invalid_get_data(invalid_date: Union[str, None, int]) -> None:
    """Тест проверки обработки невалидных данных даты."""
    with pytest.raises(ValueError):
        get_date(invalid_date)


@pytest.mark.parametrize(
    "x, expected",
    [
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Счет 09876543210987654321", "Счет **4321"),
        ("Счет 12345678987654321234", "Счет **1234"),
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
        ("Visa Electron 1234567890123456", "Visa Electron 1234 56** **** 3456"),
        ("МИР 1234567890123456", "МИР 1234 56** **** 3456"),
    ],
)
def test_valid_mask_account_card(x: str, expected: str) -> None:
    """Тест маскирования карт и счетов"""
    assert mask_account_card(x) == expected
