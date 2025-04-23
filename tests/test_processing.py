from typing import Any, Dict, List, Tuple, Union

import pytest

from main import filter_by_state, sort_by_date


def test_valid_filter_by_state(valid_filter_by_state: Tuple[List[Dict[str, Any]], str, int]) -> None:
    """Проверяем обработку валидных данных"""
    input_data, state, expected_count = valid_filter_by_state
    result: List[Dict[str, Any]] = filter_by_state(input_data, state)
    assert len(result) == expected_count
    assert all(item["state"] == state for item in result)


def test_invalid_filter_by_state(
    invalid_filter_by_state: Tuple[Union[List[Dict[str, Any]], str, List[str]], str],
) -> None:
    """Тест для невалидных данных"""
    input_data, state = invalid_filter_by_state

    if isinstance(input_data, (str, list)) and not all(isinstance(item, dict) for item in input_data):
        with pytest.raises(TypeError):
            filter_by_state(input_data, state)  # type: ignore[arg-type]
    else:
        # Для других случаев функция должна вернуть пустой список
        result: List[Dict[str, Any]] = filter_by_state(input_data, state)  # type: ignore[arg-type]
        assert result == []


def test_valid_sort_by_date(valid_sort_by_date: List[Union[Dict[str, Any], List[Dict[str, Any]]]]) -> None:
    """Проверяем, что дата в каждом словаре имеет длину 26 символов"""
    list_element: List[Dict[str, Any]] = []

    for group in valid_sort_by_date:
        if isinstance(group, list):
            list_element.extend(group)
        else:
            list_element.append(group)

    for transaction in list_element:
        date: Union[str, None] = transaction.get("date")
        assert date is not None, "Ключ 'date' отсутствует в транзакции"
        assert len(date) == 26, f"Длина даты {date} != 26"


# def test_invalid_sort_by_date(
#         invalid_sort_by_date: Tuple[Union[List[Dict[str, Any]], str], str]
# ) -> None:
#     """Проверяем обработку невалидных данных"""
#     invalid_input, expected_error = invalid_sort_by_date
#     with pytest.raises(ValueError) as exc_info:
#         sort_by_date(invalid_input)  # type: ignore[arg-type]
#     assert expected_error in str(exc_info.value)
