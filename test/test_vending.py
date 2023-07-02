from app.vending_main import calculate_order_value, change_money, compare_value, get_money, get_product
from unittest import mock
import pytest
from app.database import DB

def test_get_money():
    customer_cash = 5
    result = get_money(customer_cash)
    expected_result = customer_cash
    assert expected_result == result


@pytest.mark.parametrize(
    "customer_cash, order_value, expected_result",
    [
        (5, 5, "wydaje produkt"),
        (10, 5, "wydaję resztę i produkt"),
        (5, 10, "za mało hajsu"),
    ],
)
def test_compare_value(customer_cash, order_value, expected_result):
    result = compare_value(customer_cash, order_value)
    assert result == expected_result


@pytest.mark.parametrize(
    "customer_cash, order_value, expected_result", [(5, 5, 0), (10, 5, 5)]
)
def test_change_money_if_nothing_to_change(customer_cash, order_value, expected_result):
    result = change_money(customer_cash, order_value)
    assert result == expected_result


@pytest.mark.parametrize(
    "product_id, quantity, expected_result, expected_quantity",
    [
        (11, 1, "product_id_11", 0),
        (11, 2, "zbyt duża ilość produktu, max: 1", 1),
        (12, 1, "nie znaleziono produktu", 1),
    ],
)
def test_get_product(product_id, quantity, expected_result, expected_quantity):
    with mock.patch.dict(DB, {11:1}):
        result = get_product(product_id, quantity)
        actual_quantity = DB[11]
        assert result == expected_result
        assert actual_quantity == expected_quantity


def test_calculate_order_value():
    product = mock.MagicMock()
    product.price = 10
    order_quantity = 2
    expected_result = 20

    result = calculate_order_value(product, order_quantity)

    assert expected_result == result