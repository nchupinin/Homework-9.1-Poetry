from typing import Any, Dict, List, Tuple, Union, cast

import pytest


# Фикстура для валидных номеров карт
@pytest.fixture(
    params=[
        "1234567890123456",
        "0000000000000000",
        "9999999999999999",
        "2468013579246801",
        "5112345678901234",
        "9876543210987654",
    ]
)
def valid_card_number(request: pytest.FixtureRequest) -> str:
    return cast(str, request.param)


# Фикстура для невалидных номеров карт
@pytest.fixture(
    params=[
        (None, "Номер карты не может быть None"),
        ("", "Номер карты не может быть пустым"),
        (1234567890123456, "Номер карты должен быть строкой"),
        ("ABCDEFGHIJKLMNOP", "Номер карты должен содержать только цифры"),
        ("123", "Требуется строка из 16 цифр"),
    ]
)
def invalid_card_data(request: pytest.FixtureRequest) -> Tuple[Union[str, int, None], str]:
    return cast(Tuple[Union[str, int, None], str], request.param)


# Фикстура для валидных номеров счетов
@pytest.fixture(
    params=[
        "1234567890123456",
        "0000000000000000",
        "9999999999999999",
        "2468013579246801",
        "5112345678901234",
        "9876543210987654",
    ]
)
def valid_card_account(request: pytest.FixtureRequest) -> str:
    return cast(str, request.param)


# Фикстура для невалидных номеров счетов
@pytest.fixture(
    params=[
        (None, "Номер счета не может быть None"),
        ("", "Номер счета не может быть пустым"),
        (1234567890123456, "Номер счета должен быть строкой"),
        ("ABCDEFGHIJK", "Номер счета должен содержать только цифры"),
        ("123", "Номер счета должен содержать минимум 4 цифры"),
        ("12345678901234567", "Номер счета должен содержать не больше 16 цифр"),
    ]
)
def invalid_card_account(request: pytest.FixtureRequest) -> Tuple[Union[str, int, None], str]:
    return cast(Tuple[Union[str, int, None], str], request.param)


# Фикстура для валидных входящих данных даты
@pytest.fixture(
    params=[
        "2024-03-11T02:26:18.671407",
        "2025-10-18T01:11:12.123456",
        "2022-01-21T05:05:10.765432",
    ]
)
def valid_get_data(request: pytest.FixtureRequest) -> str:
    return cast(str, request.param)


# Фикстура для невалидных входящих данных даты
@pytest.fixture(
    params=[
        (None, "Дата не может быть None"),
        ("", "Дата не может быть пустой"),
        (1234567890123456, "Входные данные должны быть строкой"),
        ("ABCDEFGHIJKLMNOP", "Входные данные должны содержать 26 символов"),
        ("123", "Входные данные должны содержать 26 символов"),
    ]
)
def invalid_get_data(request: pytest.FixtureRequest) -> Tuple[Union[str, int, None], str]:
    return cast(Tuple[Union[str, int, None], str], request.param)


# Фикстура для валидных входящих данных
@pytest.fixture(
    params=[
        # Корректные данные (список списков словарей)
        (
            [[{"state": "EXECUTED"}, {"state": "CANCELED"}], [{"state": "EXECUTED"}]],  # list_data
            "EXECUTED",  # state
            2,  # expected_count (два элемента с EXECUTED)
        ),
        # Данные без ключа state (должны игнорироваться)
        ([[{"id": 1}, {"id": 2}], [{"state": "EXECUTED"}]], "EXECUTED", 1),  # Только один элемент подходит
    ]
)
def valid_filter_by_state(request: pytest.FixtureRequest) -> Tuple[List[List[Dict[str, Any]]], str, int]:
    return cast(Tuple[List[List[Dict[str, Any]]], str, int], request.param)


# Фикстура для невалидных входящих данных
@pytest.fixture(
    params=[
        # Невалидный тип (не список)
        ("not_a_list", "EXECUTED"),
        # Неправильная вложенность (список словарей вместо списка списков)
        ([{"id": 1}, {"id": 2}], "EXECUTED"),
    ]
)
def invalid_filter_by_state(request: pytest.FixtureRequest) -> Tuple[Union[str, List[Dict[str, Any]]], str]:
    return cast(Tuple[Union[str, List[Dict[str, Any]]], str], request.param)


@pytest.fixture(
    params=[
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            [
                {"id": 1, "state": "EXECUTED", "date": "2023-01-15T10:30:45.123456"},
                {"id": 2, "state": "PENDING", "date": "2022-12-31T23:59:59.999999"},
            ]
        ),
        (
            [
                {"id": 3, "state": "EXECUTED", "date": "2000-01-01T00:00:00.000000"},  # минимальная дата
                {"id": 4, "state": "CANCELED", "date": "2099-12-31T23:59:59.999999"},  # максимальная
            ]
        ),
        (
            [
                {"id": 5, "state": "EXECUTED", "date": "2025-05-20T15:45:30.555555"},
                {"id": 6, "state": "FAILED", "date": "2024-11-11T11:11:11.111111"},
            ]
        ),
        (
            [
                {"id": 7, "state": "EXECUTED", "date": "2021-02-28T12:34:56.789012"},
                {"id": 8, "state": "CANCELED", "date": "2020-07-04T04:20:00.000001"},
            ]
        ),
        (
            [
                {"id": 9, "state": "EXECUTED", "date": "2026-08-09T18:25:36.444444", "amount": 1000},
                {"id": 10, "state": "CANCELED", "date": "2027-03-14T09:15:22.777777", "comment": "test"},
            ]
        ),
    ]
)
def valid_sort_by_date(request: pytest.FixtureRequest) -> List[Dict[str, Any]]:
    return cast(List[Dict[str, Any]], request.param)


# @pytest.fixture(params=[
#
#     ]
# )
# def invalid_sort_by_date(request):
#     return request.param
