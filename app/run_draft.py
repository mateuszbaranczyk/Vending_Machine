from app import vending_operations
from app.database import DB


def avaliability(customer_order: int, ordered_quantity: int) -> object:
    while True:
        avaliable_msg = vending_operations.check_avaliabity(customer_order, ordered_quantity)

        if f"{customer_order}" in avaliable_msg:
            product = DB.get(customer_order)
            break
        else:
            print(avaliable_msg)
            customer_order = int(input("wybierz produkt "))
            continue
    return product


def cash(ordered_quantity: int, customer_cash: int, product: object):
    while True:
        order_value = vending_operations.calculate_order_value(product, ordered_quantity)
        cash_msg = vending_operations.compare_value(customer_cash, order_value)

        if cash_msg == "wydaje produkt" or "wydaję resztę i produkt":
            product.give_quantity(ordered_quantity)
            print(cash_msg)
            break
        else:
            print(cash_msg)
            customer_cash = int(input("wrzuć monete "))
            continue
    return order_value


def run():
    customer_order = int(input("wybierz produkt "))
    ordered_quantity = int(input("podaj ilość "))
    customer_cash = int(input("wrzuć monete "))
    product = avaliability(customer_order, ordered_quantity)
    order_value = cash(ordered_quantity, customer_cash, product)
    change = vending_operations.change_money(customer_cash, order_value)
    print(f"reszta: {change} pieniędzy")


if __name__ == "__main__":
    run()
