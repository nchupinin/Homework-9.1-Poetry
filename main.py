from src.widget.mask_account_card import get_mask_account, get_mask_card_number, get_date
from src.processing import filter_by_state#, sort_by_date

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


    list_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    list_data_key_state = filter_by_state(list_data)
    print("Список 'EXECUTED':", list_data_key_state)

    list_sort_data = sort_by_date(list_data)
    print("Cписок, отсортированный по дате:", list_sort_data)


if __name__ == "__main__":
    main()
