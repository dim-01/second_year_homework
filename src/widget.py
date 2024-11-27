from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card):
    if account_card[:4] == "Счет":
        return f"{account_card[:-21]} {get_mask_account(account_card[-20:])}"
    else:
        return f"{account_card[:-17]} {get_mask_card_number(account_card[-16:])}"
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(date_string):
    date_parts = date_string.split("T")
    return date_parts[0].split("-")[2] + "." + date_parts[0].split("-")[1] + "." + date_parts[0].split("-")[0]

print(get_date("2024-03-11T02:26:18.671407"))