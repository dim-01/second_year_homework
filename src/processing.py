<<<<<<< HEAD
def filter_by_state(data: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей для фильтрации.
    :param state: Значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список словарей.
    """
    return [item for item in data if item.get("state") == state]

def sort_by_date(data, reverse=True):
    """
    Сортирует список словарей по дате (ключ 'date').

    :param data: Список словарей для сортировки.
    :param reverse: Флаг сортировки по убыванию (по умолчанию True).
    :return: Отсортированный список словарей.
    """
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
=======
def filter_by_state(my_list, state='EXECUTED'):
    """Функция  принимает номер карты и возвращает ее маскотораяку"""
    return [d for d in my_list if d['state'] == state]


def sort_by_date(data, order='DESC'):
    if order not in ('ASC', 'DESC'):
        order = 'DESC'
    return sorted(data, key=lambda d: d['date'], reverse=order == 'DESC')
>>>>>>> 23d2b550ba756891930afee6e7bfa2fa0d63bcfe
