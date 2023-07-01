from app.vending_main import change_money, compare_value, get_money
import pytest


def test_get_money():
    customer_cash = 5
    result = get_money(customer_cash)
    expected_result = customer_cash
    assert expected_result == result


@pytest.mark.parametrize(
    "customer_cache, order_value, expected_result",
    [
        (5, 5, "wydaje produkt"),
        (10, 5, "wydaję resztę i produkt"),
        (5, 10, "za mało hajsu"),
    ],
)
def test_compare_value(customer_cache, order_value, expected_result):
    result = compare_value(customer_cache, order_value)
    assert result == expected_result


@pytest.mark.parametrize(
    "customer_cache, order_value, expected_result", [(5, 5, 0), (10, 5, 5)]
)
def test_change_money_if_nothing_to_change():
    customer_cash = 5
    order_value = 5
    expected_result = 0
    result = change_money(customer_cash, order_value)
    assert result == expected_result


def test_change_money_if_cash_to_return():
    customer_cash = 10
    order_value = 5
    expected_result = 5
    result = change_money(customer_cash, order_value)
    assert result == expected_result
