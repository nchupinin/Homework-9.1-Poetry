import pytest

from main import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "valid_card_number",
    [
        ("123456789012345612"),
        ("0000000000000000000"),
        ("9999999999999999999"),
        ("2468013579246801098"),
        ("5112345678901234"),
        ("987654321098765"),
    ],
)
def test_valid_get_mask_card_number(valid_card_number: str) -> None:
    """Тест валидных номеров карт"""
    assert len(valid_card_number) < 20


@pytest.mark.parametrize(
    "invalid_card_number",
    [
        "12345678910",  # Номер карты не может быть меньше 10 цифр
        r"!№?%-_=+.,/\:№!:;№!?:;",  # Номер карты не может состоять из символов
        "фущкгпидыукгпзцук",  # Номер карты не может состоять из букв
        "",  # Пустая строка
        None,  # "Номер карты не может быть None"
        131249765142,  # "Номер карты должны быть строкой"
    ],
)
def test_invalid_get_mask_card_number(invalid_card_number: str) -> None:
    """Тест невалидных номеров карт"""
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card_number)


@pytest.mark.parametrize(
    "valid_account",
    [
        "12345678901234561823",
        "00000000000000000000",
        "99999999999999999999",
        "246801357924680311",
        "5112345678901234123",
        "98765432109876543",
    ],
)
def test_valid_get_mask_account(valid_account: str) -> None:
    """Тест валидных номеров счетов"""
    assert 4 <= len(valid_account) <= 20


@pytest.mark.parametrize(
    "invalid_account",
    [
        None,
        "",
        1342452353425,
        "YGyuborygoyhfe",
        "123456789012345678901",
        "123",
    ],
)
def test_invalid_get_mask_account(invalid_account: str) -> None:
    """Тест невалидных номеров счетов"""
    with pytest.raises(ValueError):
        get_mask_account(invalid_account)
