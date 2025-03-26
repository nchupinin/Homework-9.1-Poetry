from src.masks.card import get_mask_account, get_mask_card_number


def main():
    """Возвращает маскированный номер карты и маску счета """

    card_number = "7080792289066543"
    masked_card = get_mask_card_number(card_number)
    print("Маскированный номер карты:", masked_card)

    account_number = "1234567890123456"
    masked_account = get_mask_account(account_number)
    print("Маскированный номер счета:", masked_account)


if __name__ == "__main__":
    main()
