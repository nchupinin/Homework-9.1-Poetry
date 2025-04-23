def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате 'XXXX XX** **** XXXX'"""

    if card_number is None:
        raise ValueError("Номер карты не может быть None")

    if card_number == "":
        raise ValueError("Номер карты не может быть пустым")

    if not isinstance(card_number, str):
        raise ValueError("Номер карты должен быть строкой")

    if not card_number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    if len(card_number) != 16:
        raise ValueError("Требуется строка из 16 цифр")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета (показывает только последние 4 цифры)"""

    if account_number is None:
        raise ValueError("Номер счета не может быть None")

    if account_number == "":
        raise ValueError("Номер счета не может быть пустым")

    if not isinstance(account_number, str):
        raise ValueError("Номер счета должен быть строкой")

    if not account_number.isdigit():
        raise ValueError("Номер счета должен содержать только цифры")

    if len(account_number) > 16:
        raise ValueError("Номер счета должен содержать не больше 16 цифр")

    if len(account_number) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{account_number[-4:]}"


def get_date(date: str) -> str:
    """Возвращает строку с датой в формате ДД.ММ.ГГГГ (11.03.2024)."""

    if date is None:
        raise ValueError("Дата не может быть None")

    if date == "":
        raise ValueError("Дата не может быть пустой")

    if not isinstance(date, str):
        raise ValueError("Входные данные должны быть строкой")

    if len(date) != 26:
        raise ValueError("Входные данные должны содержать 26 символов")

    result = f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    return result
