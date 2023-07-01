from app.vending_main import change_money, compare_value, get_money, get_product
import pytest


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
def test_change_money_if_nothing_to_change(
    customer_cash, order_value, expected_result
):
    result = change_money(customer_cash, order_value)
    assert result == expected_result

@pytest.patch("app.database.DB")
def test_get_product(db):
    db.return_value = {11:1}
    product_id = 11
    quantity = 1
    expected_result = "wydano produkt"
    result = get_product(product_id, quantity)
    assert result == expected_result
    