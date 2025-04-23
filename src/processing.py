from datetime import datetime
from typing import Any, Dict, List, Tuple, Union


def filter_by_state(
    list_data: Union[List[Dict[str, Any]], Tuple[List[Dict[str, Any]], ...], List[List[Dict[str, Any]]]],
    state: str = "EXECUTED",
) -> List[Dict[str, Any]]:
    """
    Фильтрует операции по статусу.
    Поддерживает:
    - Плоский список: [op1, op2]
    - Кортеж списков: ([op1, op2], [op3])
    - Список списков: [[op1, op2], [op3]]
    """
    result: List[Dict[str, Any]] = []

    # Если данные в кортеже или списке списков
    if isinstance(list_data, (tuple, list)) and all(isinstance(sublist, list) for sublist in list_data):
        for sublist in list_data:
            result.extend(op for op in sublist if isinstance(op, dict) and op.get("state") == state)
    # Если плоский список
    elif isinstance(list_data, list):
        result = [op for op in list_data if isinstance(op, dict) and op.get("state") == state]
    else:
        raise TypeError("Ожидается список/кортеж операций или вложенные списки")

    return result


def sort_by_date(list_data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Возвращает новый список, отсортированный по дате
    True (по умолчанию), сортирует по убыванию (новые → старые)."""
    return sorted(list_data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
