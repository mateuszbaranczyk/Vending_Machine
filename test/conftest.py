from pytest import fixture

from app.database import Product


@fixture
def product():
    product = Product(product_id=11, unit_price=10, quantity=50)
    return product
