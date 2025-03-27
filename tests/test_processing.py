import pytest
from src.processing import filter_by_state

@pytest.mark.parametrize("state, expected_ids", [
    ("EXECUTED", [1, 3]),  # Фильтрация по EXECUTED
    ("CANCELED", [2]),  # Фильтрация по CANCELED
    ("PENDING", [4]),  # Фильтрация по PENDING
    ("UNKNOWN", []),  # Неизвестный статус
])
def test_filter_by_state(sample_data, state, expected_ids):
    result = filter_by_state(sample_data, state)
    assert [item["id"] for item in result] == expected_ids


from src.processing import sort_by_date

def test_sort_by_date_ascending(sample_data):
    result = sort_by_date(sample_data, reverse=False)
    assert [item["id"] for item in result] == [2, 3, 4, 1]  # По возрастанию даты

def test_sort_by_date_descending(sample_data):
    result = sort_by_date(sample_data, reverse=True)
    assert [item["id"] for item in result] == [1, 4, 3, 2]  # По убыванию даты