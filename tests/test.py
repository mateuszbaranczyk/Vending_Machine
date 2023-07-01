from app.vending_main import change_money, compare_value, get_money


def test_get_money():
    customer_cash = 5
    result = get_money(customer_cash)
    expected_result = customer_cash
    assert expected_result == result


def test_compare_value():
    customer_cache = 5
    order_value = 5
    expected_result = "wydaje produkt"
    result = compare_value(customer_cache, order_value)
    assert result == expected_result


def test_compare_value_2():
    customer_cache = 10
    order_value = 5
    expected_result = "wydaję resztę i produkt"
    result = compare_value(customer_cache, order_value)
    assert result == expected_result


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
