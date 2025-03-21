import pytest
from src.widget import mask_account_card

@pytest.mark.parametrize("input_data, expected", [
    ("Счет 1234567890", "Счет **7890"),
    ("Карта 1234567812345678", "Карта 1234 56** **** 5678"),
    ("Некорректные данные", "Некорректные данные"),  # Некорректные входные данные
])
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected


from src.widget import get_date

@pytest.mark.parametrize("input_date, expected", [
    ("2023-10-01T12:34:56.789", "01.10.2023"),
    ("2022-12-31T23:59:59.999", "31.12.2022"),
    ("", ""),  # Граничный случай: пустая строка
])
def test_get_date(input_date, expected):
    assert get_date(input_date) == expected