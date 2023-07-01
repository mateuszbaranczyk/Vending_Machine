from unittest import mock

def test_get_money():
    insert_cash = mock.MagicMock(return_value=3)
    compare_value = mock.MagicMock(return_value=0)
    change_money = mock.MagicMock(return_value=0)
    
    
def test_get_money():
    customer_cash = 5
    get_money = get_money(customer_cash)
    expected_result = customer_cash
    assert expected_result == customer_cash