import pytest

from shoppingcart.classes.Sale import Sale
from shoppingcart.classes.Item import Item


def test_instantiation_item_object(raw_sale):
    result = raw_sale
    expected = Sale(Item(_name='banana', _code=1, _price=1.1), 1, 1.1)
    assert result == expected

def test_instantiation_object_should_fail():
    with pytest.raises(TypeError) as e:
        c = Item()
        error_msg = "Item.__init__() missing 1 required positional arguments: '_item'"
        assert str(e.value) == error_msg

def test_quantity_shouldnt_be_less_than_one(raw_item):
    with pytest.raises(Exception) as e:
        Sale(Item(**raw_item), 0)
        error_msg = "The quantity of a product been sold should be greater than 0 or less"
        assert str(e.value) == error_msg

def test_calc_total_price_on_instantiation(raw_sale_more_than_one):
    result = raw_sale_more_than_one.total_price
    expected = 2.2
    assert result == expected

def test_update_quantity_on_instantiation(raw_sale_more_than_one):
    result = raw_sale_more_than_one.quantity
    expected = 2
    assert result == expected

def test_getter_item(raw_sale):
    result = raw_sale.item
    expected = Item(_name='banana', _code=1, _price=1.10)
    assert result == expected

def test_getter_item_is_instance_item_class(raw_sale):
    assert isinstance(raw_sale.item, Item)

def test_getter_item_check_if_id_od_private_attribute_is_the_same_returned(raw_sale):
    result = id(raw_sale.item)
    expected = id(raw_sale._item)
    assert result == expected

def test_getter_quantity(raw_sale):
    result = raw_sale.quantity
    expected = 1
    assert result == expected

def test_getter_quantity_check_if_id_of_private_attribute_is_the_same(raw_sale):
    result = id(raw_sale.quantity)
    expected = id(raw_sale._quantity)
    assert result == expected

def test_getter_total_price(raw_sale):
    result = raw_sale.total_price
    expected = 1.1
    assert result == expected

def test_getter_total_price_check_if_id_of_private_attribute_is_the_same(raw_sale):
    result = id(raw_sale.total_price)
    expected = id(raw_sale._total_price)
    assert result == expected

def test_quantity_setter(raw_sale):
    raw_sale.quantity = 7
    result = raw_sale.quantity
    expected = 7
    assert result == expected

def test_calc_total_price_update_total_price(raw_sale):
    raw_sale.calc_total_price(7)
    result = raw_sale.total_price
    expected = 7 * 1.1
    assert result == expected

def method_repr_to_shade_private_attributes(raw_sale):
    result = str(raw_sale.__rep__())
    expected = 'Sale(Item(name=banana, code=1, price=1.10), quantity=1, total_price=1.10)'
    assert result == expected

def str_method_to_get_price_list(raw_sale, banana):
    result = str(raw_sale)
    expected = banana
    assert result == expected




