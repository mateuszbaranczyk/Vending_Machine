from dataclasses import dataclass

DB = {11:50}

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