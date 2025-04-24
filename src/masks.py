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


