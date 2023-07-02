from dataclasses import dataclass


@dataclass
class Product:
    product_id: int
    unit_price: int
    quantity: int

    def __repr__(self) -> str:
        return f"product_id_{self.product_id}"

    def give_quantity(self, ordered_quantity):
        new_quantity = self.quantity - ordered_quantity
        setattr(self, "quantity", new_quantity)
        return new_quantity


product = Product(product_id=11, unit_price=10, quantity=50)
DB = {11: product}
