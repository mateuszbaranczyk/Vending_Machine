from unittest.mock import patch, Mock
from app.database import DB
from app.vending_main import VendingMashine
import builtins


mocked_input = Mock()
mocked_input.side_effect = [11, 1, 10]


@patch.object(builtins, "input", mocked_input)
def test_vending_main(product):
    product.quantity = 1
    with patch.dict(DB, {11: product}):
        vending = VendingMashine()
        vending.__call__()
        actual_quantity = DB[11].quantity

    assert actual_quantity == 0
