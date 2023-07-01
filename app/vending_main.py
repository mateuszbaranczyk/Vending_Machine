def get_money(customer_cash: int) -> int:
    return customer_cash


def change_money(customer_cash: int, order_value: int) -> int:
    value_return = customer_cash - order_value
    if value_return <= 0:
        value_return = 0
    return value_return


def compare_value(customer_cash: int, order_value: int) -> str:
    if customer_cash < order_value:
        return "za mało hajsu"
    elif customer_cash > order_value:
        return "wydaję resztę i produkt"
    else:
        return "wydaje produkt"


def get_product(product_id, quantity):
    # odejmowanie stanów magazynowych
    pass
