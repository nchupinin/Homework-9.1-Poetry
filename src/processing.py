from datetime import datetime
from typing import Dict, List


def filter_by_state(list_data: list) -> list:
    """Возвращает список словарей, где state == 'EXECUTED'."""

    new_list = []
    for sublist in list_data:
        for item in sublist:
            if item.get("state") == "EXECUTED":
                new_list.append(item.copy())
    return new_list


def sort_by_date(list_data: list[dict], reverse: bool = True) -> list[dict]:
    """Возвращает новый список, отсортированный по дате
    True (по умолчанию), сортирует по убыванию (новые → старые)."""

    flat_list = [item for sublist in list_data for item in sublist]
    return sorted(flat_list, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
