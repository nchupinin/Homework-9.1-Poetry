from typing import Tuple, Union

import pytest

from main import get_date, get_mask_account, get_mask_card_number


def test_get_mask_card_number(valid_card_number: str) -> None:
    """Проверяем обработку валидных номеров карт"""
    assert len(valid_card_number) == 16


def test_invalid_card_numbers(invalid_card_data: Tuple[str, str]) -> None:
    """Тестируем обработку ошибок"""
    invalid_input, expected_error = invalid_card_data
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(invalid_input)
    assert expected_error in str(exc_info.value)


def test_valid_account_numbers(valid_card_account: str) -> None:
    """Проверяем обработку валидных номеров счета"""
    assert 4 <= len(valid_card_account) <= 16


def test_invalid_account_numbers(invalid_card_account: Tuple[str, str]) -> None:
    """Тестируем обработку ошибок номеров счетов"""
    invalid_input, expected_error = invalid_card_account
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(invalid_input)
    assert expected_error in str(exc_info.value)


def test_valid_get_data(valid_get_data: str) -> None:
    """Проверяем обработку данных даты"""
    assert len(valid_get_data) == 26


def test_invalid_get_data(invalid_get_data: Tuple[Union[str, int], str]) -> None:
    """Тестируем обработку ошибок входящих данных"""
    invalid_input, expected_error = invalid_get_data
    with pytest.raises(ValueError) as exc_info:
        get_date(invalid_input)
    assert expected_error in str(exc_info.value)
