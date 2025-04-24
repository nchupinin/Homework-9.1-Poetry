from typing import Any, Dict, List, Tuple, Union

import pytest

from main import filter_by_state, sort_by_date


@pytest.mark.parametrize("list_data, state, expected_count", [
    # список списков словарей
    (
            [[{"state": "EXECUTED"}, {"state": "CANCELED"}], [{"state": "EXECUTED"}]],  # list_data
            "EXECUTED",  # state
            2,  # expected_count (два элемента с EXECUTED)
    ),
    # данные без ключа state должны игнорироваться
    (
            [[{"id": 1}, {"id": 2}], [{"state": "EXECUTED"}]],  # list_data
            "EXECUTED",  # state
            1,  # expected_count (только один элемент подходит)
    ),
])
def test_valid_filter_by_state(
        list_data: List[List[Dict[str, Any]]],
        state: str,
        expected_count: int
) -> None:
    """Тест валидных данных для фильтрации по статусу"""
    # Распаковываем вложенные списки в один плоский список
    flat_list = [item for sublist in list_data for item in sublist]

    # Фильтруем по state (если ключ существует)
    filtered = [d for d in flat_list if d.get("state") == state]

    assert len(filtered) == expected_count


@pytest.mark.parametrize("invalid_data, state, expected_exception", [
    # Невалидный тип (не список и не кортеж)
    ("not_a_list", "EXECUTED", TypeError),
    # Другие невалидные типы
    (12345, "EXECUTED", TypeError),
    ({"key": "value"}, "EXECUTED", TypeError),
    # Некорректная вложенность (кортеж не списков)
    (({"id": 1}, {"id": 2}), "EXECUTED", TypeError),
])
def test_invalid_filter_by_state(
    invalid_data: Any,
    state: str,
    expected_exception: type[Exception],
) -> None:
    """Тест обработки невалидных входных данных"""
    with pytest.raises(expected_exception):
        filter_by_state(invalid_data, state)



@pytest.mark.parametrize("valid_sort_by_date", [
    # Первый случай - выполненные и отмененные операции
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ],
    # Второй случай - выполненные и ожидающие операции
    [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-15T10:30:45.123456"},
        {"id": 2, "state": "PENDING", "date": "2022-12-31T23:59:59.999999"},
    ],
    # Третий случай - минимальная и максимальная даты
    [
        {"id": 3, "state": "EXECUTED", "date": "2000-01-01T00:00:00.000000"},
        {"id": 4, "state": "CANCELED", "date": "2099-12-31T23:59:59.999999"},
    ],
    # Четвертый случай - разные статусы
    [
        {"id": 5, "state": "EXECUTED", "date": "2025-05-20T15:45:30.555555"},
        {"id": 6, "state": "FAILED", "date": "2024-11-11T11:11:11.111111"},
    ],
    # Пятый случай - разные даты
    [
        {"id": 7, "state": "EXECUTED", "date": "2021-02-28T12:34:56.789012"},
        {"id": 8, "state": "CANCELED", "date": "2020-07-04T04:20:00.000001"},
    ],
    # Шестой случай - операции с дополнительными полями
    [
        {"id": 9, "state": "EXECUTED", "date": "2026-08-09T18:25:36.444444", "amount": 1000},
        {"id": 10, "state": "CANCELED", "date": "2027-03-14T09:15:22.777777", "comment": "test"},
    ],
])
def test_valid_sort_by_date(valid_sort_by_date: List[Dict[str, Any]]) -> None:
    """Тест сортировки валидных данных по дате"""
    sorted_ops = sorted(valid_sort_by_date, key=lambda x: x["date"], reverse=True)
    assert len(sorted_ops) == len(valid_sort_by_date)
    assert sorted_ops[0]["date"] >= sorted_ops[-1]["date"]


@pytest.mark.parametrize("invalid_operations, expected_exception", [
    # Нет ключа 'date'
    ([{"id": 1, "state": "EXECUTED"}], KeyError),
    # Неправильный формат даты (оставляем только явно невалидные)
    ([{"id": 3, "state": "EXECUTED", "date": "не_дата"}], ValueError),
    # Не список операций
    ("not_a_list", TypeError),
    (12345, TypeError),
    ({"key": "value"}, TypeError),
    # None вместо списка
    (None, TypeError),
    # Поврежденные данные
    ([None], TypeError),
])
def test_invalid_sort_by_date(invalid_operations: Any, expected_exception: type[Exception]) -> None:
    """Тест обработки действительно невалидных данных"""
    with pytest.raises(expected_exception):
        sort_by_date(invalid_operations)



