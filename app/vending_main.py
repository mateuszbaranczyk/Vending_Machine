from app.database import DB


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


def check_avaliabity(product_id: int, ordered_quantity: int) -> str:
    product = DB.get(product_id, None)

    if not product:
        return "nie znaleziono produktu"

    if ordered_quantity > product.quantity:
        return f"zbyt duża ilość produktu, max: {product.quantity}"

    product.give_quantity(ordered_quantity)
    return str(product)


def calculate_order_value(product: object, order_quantity: int) -> int:
    order_value = product.price * order_quantity
    return order_value
