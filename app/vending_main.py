def get_money(customer_cash: int) -> int:
    return customer_cash


def change_money(value_return, order_value: int):
    return value_return


def compare_value(customer_cash: int, order_value: int) -> str:
    if customer_cash < order_value:
        return "za mało hajsu"
    elif customer_cash > order_value:
        return "wydaję resztę i produkt"
    else:
        return "wydaje produkt"
