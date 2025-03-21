def filter_by_state(my_list, state='EXECUTED'):
    """Функция  принимает номер карты и возвращает ее маскотораяку"""
    return [d for d in my_list if d['state'] == state]


def sort_by_date(data, order='DESC'):
    if order not in ('ASC', 'DESC'):
        order = 'DESC'
    return sorted(data, key=lambda d: d['date'], reverse=order == 'DESC')
