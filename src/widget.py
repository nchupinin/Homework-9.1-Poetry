from src.masks import get_mask_account, get_mask_card_number


def get_date(date: str) -> str:
    """Возвращает строку с датой в формате ДД.ММ.ГГГГ (11.03.2024)."""

    # Проверка на None и не-строку
    if date is None:
        raise ValueError("Дата не может быть None")
    if not isinstance(date, str):
        raise ValueError("Входные данные должны быть строкой")

        # Проверка пустой строки
    if not date:
        raise ValueError("Пустая строка")

        # Проверка случайной строки (без цифр)
    if date.isalpha():
        raise ValueError("Случайная строка")

        # Проверка длины (строго 26 символов)
    if len(date) != 26:
        raise ValueError("Входные данные должны содержать 26 символов")

        # Проверка формата даты (YYYY-MM-DDTHH:MM:SS.ffffff)
    if len(date) < 10 or date[4] != "-" or date[7] != "-":
        raise ValueError("Неправильный формат даты (должен быть YYYY-MM-DD...)")

        # Проверка месяца и дня
    try:
        month = int(date[5:7])
        day = int(date[8:10])
    except ValueError:
        raise ValueError("Неверный формат чисел в дате")

    if month > 12:
        raise ValueError("Количество месяцев не может превышать 12")
    if day > 31:
        raise ValueError("Количество дней не может превышать 31")
    # Форматирование результата
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


def mask_account_card(info: str) -> str:
    """Маскирует номер счета или номер карты разными способами
    в зависимости от того какие данные приходят на вход"""

    parts_numbers = info.split()
    number = parts_numbers[-1]
    card_name = " ".join(parts_numbers[:-1])

    if info.startswith("Счет"):
        stealth_number = get_mask_account(number)

    else:
        stealth_number = get_mask_card_number(number)
    return f"{card_name} {stealth_number}"
