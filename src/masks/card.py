def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате 'XXXX XX** **** XXXX'"""

    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Требуется строка из 16 цифр")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета (показывает только последние 4 цифры)"""

    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{account_number[-4:]}"
