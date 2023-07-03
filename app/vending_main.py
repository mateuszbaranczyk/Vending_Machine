from app.database import DB
from app.vending_operations import (
    calculate_order_value,
    change_money,
    check_avaliabity,
    compare_value,
)


class VendingMashine:
    def __init__(self) -> None:
        self.db = DB

    def __call__(self) -> None:
        self.get_order()
        self.calculate_money()
        self.deliver_order_and_change()

    def get_order(self) -> None:
        self.customer_order = int(input("wybierz produkt "))
        self.ordered_quantity = int(input("podaj ilość "))
        while True:
            avaliable_msg = check_avaliabity(self.customer_order, self.ordered_quantity)

            if f"{self.customer_order}" in avaliable_msg:
                self.product = DB.get(self.customer_order)
                break
            else:
                print(avaliable_msg)
                self.customer_order = int(input("wybierz produkt "))
                continue

    def calculate_money(self) -> None:
        self.customer_cash = int(input("wrzuć monete "))
        while True:
            self.order_value = calculate_order_value(
                self.product, self.ordered_quantity
            )
            cash_msg = compare_value(self.customer_cash, self.order_value)

            if cash_msg == "wydaje produkt" or "wydaję resztę i produkt":
                print(cash_msg)
                break
            else:
                print(cash_msg)
                self.customer_cash = int(input("wrzuć monete "))
                continue

    def deliver_order_and_change(self) -> None:
        self.product.give_quantity(self.ordered_quantity)
        change = change_money(self.customer_cash, self.order_value)
        print(f"reszta: {change} pieniędzy")


if __name__ == "__main__":
    vending_machine = VendingMashine()
    vending_machine.__call__()
