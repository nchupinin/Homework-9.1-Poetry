from typing import Iterator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Iterator[dict]:
    """Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной валюте"""
    for transaction in transactions:
        try:
            operation_amount = transaction.get("operationAmount", {})
            if isinstance(operation_amount, dict):
                curr = operation_amount.get("currency", {})
                if isinstance(curr, dict) and curr.get("code") == currency_code:
                    yield transaction
        except (AttributeError, TypeError):
            continue


def transaction_descriptions(transactions: list[dict]) -> str:
    """Возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int = 1, stop: int = None) -> list:
    """Выдает последовательные номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    if not isinstance(start, int) or (stop is not None and not isinstance(stop, int)):
        raise TypeError("`start` и `stop` должны быть целыми числами")
    if start < 1 or (stop is not None and stop < 1):
        raise ValueError("`start` и `stop` должны быть >= 1")

    current = start
    while stop is None or current < stop:
        yield f"{current:016d}"
        current += 1
