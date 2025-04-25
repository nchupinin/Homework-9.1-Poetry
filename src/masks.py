def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате 'XXXX XX** **** XXXX'"""

    # Проверка на None
    if card_number is None:
        raise ValueError("Номер карты не может быть None")

    if not isinstance(card_number, str):
        raise ValueError("Номер карты должен быть строкой")

    cleaned_number = card_number.replace(" ", "")

    if not cleaned_number:
        raise ValueError("Номер карты не может быть пустым")

    if not cleaned_number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    # Стандартные номера карт: 13-19 цифр
    if len(cleaned_number) < 13 or len(cleaned_number) > 19:
        raise ValueError("Номер карты должен содержать от 13 до 19 цифр")

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

    if len(account_number) > 20:
        raise ValueError("Номер счета должен содержать не больше 20 цифр")

    if len(account_number) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{account_number[-4:]}"
