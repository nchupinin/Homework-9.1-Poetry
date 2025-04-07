from src.widget.mask_account_card import get_mask_account, get_mask_card_number, get_date


def main():
    """Возвращает маскированный номер карты, маску счета и дату"""

    card_number = "7080792289066543"
    masked_card = get_mask_card_number(card_number)
    print("Маскированный номер карты:", masked_card)

    account_number = "1234567890123456"
    masked_account = get_mask_account(account_number)
    print("Маскированный номер счета:", masked_account)

    data_number = "2024-03-11T02:26:18.671407"
    data = get_date(data_number)
    print("Дата банковской операции со счетом:",data)

if __name__ == "__main__":
    main()
