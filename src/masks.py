def get_mask_card_number(card_number: str) -> str:
    """Функция  принимает номер карты и возвращает ее маскотораяку"""
    if not card_number:
        return ""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция которая принимает номер счета и возвращает ее маску"""
    if not account_number:
        return ""
    return f"**{account_number[-4:]}"
