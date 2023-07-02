from app.database import Product


def test_product_dataclass():
    product_id = 11
    unit_price = 10
    quantity = 50

    product = Product(product_id, unit_price, quantity)

    assert product.product_id == product_id
    assert product.unit_price == unit_price
    assert product.quantity == quantity


def test_give_quantity(product):
    result = product.give_quantity(2)
    expected_result = 48
    assert result == expected_result
    assert product.quantity == expected_result
