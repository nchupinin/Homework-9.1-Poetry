import pytest

from src.generators import card_number_generator, filter_by_currency


# Фикстура с полными данными транзакций
@pytest.fixture
def sample_transactions():
    return [
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


# Параметризованный тест
@pytest.mark.parametrize(
    "currency,expected_count,expected_ids",
    [
        ("USD", 3, [939719570, 142264268, 895315941]),  # 3 USD-транзакции
        ("RUB", 2, [873106923, 594226727]),  # 2 RUB-транзакции
        ("EUR", 0, []),  # Нет EUR-транзакций
        ("GBP", 0, []),  # Нет GBP-транзакций
    ],
)
def test_filter_by_currency(sample_transactions, currency, expected_count, expected_ids):
    # Получаем результат
    result = list(filter_by_currency(sample_transactions, currency))

    # Проверяем количество транзакций
    assert len(result) == expected_count

    # Проверяем ID транзакций (если expected_count > 0)
    if expected_count > 0:
        assert [tx["id"] for tx in result] == expected_ids

    # Дополнительная проверка для EXECUTED-транзакций
    if currency == "USD":
        assert all(tx["state"] == "EXECUTED" for tx in result)


pytest.mark.parametrize(
    "expected_descriptions",
    [
        (["Перевод организации", "Оплата услуг", "Пополнение счета"]),
        (["Перевод организации", "Оплата услуг"]),
        (["Пополнение счета"]),
    ],
)


@pytest.mark.parametrize(
    "expected_descriptions",
    [
        (
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
            ]
        ),
    ],
)
def test_transaction_descriptions(sample_transactions, expected_descriptions):
    # Получаем список описаний из фикстуры
    descriptions = [tx["description"] for tx in sample_transactions]

    # Проверяем соответствие ожидаемым описаниям
    assert descriptions == expected_descriptions


def test_valid_card_number_generator():
    """Тест генератора карт валидных данных"""
    generator = card_number_generator()
    assert next(generator) == "0000000000000001"
    assert next(generator) == "0000000000000002"
    assert next(generator) == "0000000000000003"
    assert next(generator) == "0000000000000004"
    assert next(generator) == "0000000000000005"
    assert next(generator) == "0000000000000006"
    assert next(generator) == "0000000000000007"
    assert next(generator) == "0000000000000008"
    assert next(generator) == "0000000000000009"
    assert next(generator) == "0000000000000010"
    assert next(generator) == "0000000000000011"
    assert next(generator) == "0000000000000012"
    assert next(generator) == "0000000000000013"
    assert next(generator) == "0000000000000014"
    assert next(generator) == "0000000000000015"
    assert next(generator) == "0000000000000016"
    assert next(generator) == "0000000000000017"
    assert next(generator) == "0000000000000018"
    assert next(generator) == "0000000000000019"
    assert next(generator) == "0000000000000020"

    # Тест с указанием start и stop
    limited_generator = card_number_generator(start=100, stop=105)
    assert list(limited_generator) == [
        "0000000000000100",
        "0000000000000101",
        "0000000000000102",
        "0000000000000103",
        "0000000000000104",
    ]


@pytest.mark.parametrize(
    "invalid_input, expected_error",
    [
        (None, TypeError),
        ("1234", TypeError),
        (0, ValueError),
        (1.5, TypeError),
        (-1, ValueError),
    ],
)
def test_invalid_card_number_generator(invalid_input, expected_error):
    """Тест генератора карт невалидных данных"""
    with pytest.raises(expected_error):
        next(card_number_generator(start=invalid_input))
