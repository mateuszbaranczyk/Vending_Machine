from unittest import mock

from app.vending_main import change_money, compare_value, get_money

def test_get_money():
    insert_cash = mock.MagicMock(return_value=3)
    compare_value = mock.MagicMock(return_value=0)
    change_money = mock.MagicMock(return_value=0)
    
    
def test_get_money():
    customer_cash = 5
    result = get_money(customer_cash)
    expected_result = customer_cash
    assert expected_result == result

def test_compare_value():
    customer_cache= 5
    order_value = 5
    expected_result = "wydaje produkt"
    result = compare_value(customer_cache, order_value)
    assert result == expected_result

def test_change_money():
    customer_cash = 5
    order_value = 5
    expected_result = 0
    result = change_money(customer_cash, order_value)
    assert result == expected_result