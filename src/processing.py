def  filter_by_state(list_data: list) -> list:
    '''Возвращает список словарей, где state == 'EXECUTED'.'''

    new_list = []
    for sublist in list_data:
        for item in sublist:
            if item.get("state") == "EXECUTED":
                new_list.append(item.copy())
    return new_list


def sort_by_date(list_data: list) -> list:
    '''Возвращает новый список, отсортированный по дате'''



