def get_mask_card_number(card_number: str) -> str:
    """Функция  принимает номер карты и возвращает ее маскотораяку"""
    masked_card_number = card_number[:4] + " " + card_number[4:6] + "**" + " " + "****" " " + card_number[-4:]
    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """Функция которая принимает номер счета и возвращает ее маску"""
    masked_account_number = "**" + account_number[-4:]
    return masked_account_number
