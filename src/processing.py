from typing import List, Dict

def filter_by_state(data: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return [item for item in data if item.get("state") == state]

def sort_by_date(data: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """
    Сортирует список словарей по дате (ключ 'date').
    """
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
