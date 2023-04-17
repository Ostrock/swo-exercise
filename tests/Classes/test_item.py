import pytest 
from shoppingcart.classes.Item import Item

def test_instantiation_item_object(raw_item):
    result = Item(**raw_item)
    expected = Item(_name='banana', _code=1, _price=1.1)
    assert result == expected

def test_instantiation_object_should_fail():
    with pytest.raises(TypeError) as e:
        c = Item()
        error_msg = "Item.__init__() missing 3 required positional arguments: '_name', '_code', and '_price'"
        assert str(e.value) == error_msg

def test_code_valid():
    result = Item.code_validator('456')
    expected = 456
    assert result == expected

def test_code_valid_beggins_with_spaces():
    result = Item.code_validator(' 456')
    expected = 456
    assert result == expected

def test_code_valid_ends_with_space():
    result = Item.code_validator('456 ')
    expected = 456
    assert result == expected

def test_code_valid_begins_and_ends_with_space():
    result = Item.code_validator('456 ')
    expected = 456
    assert result == expected

def test_code_validator_with_non_int_string_should_fail():
    with pytest.raises(Exception) as e:
        Item.code_validator('45f')
        error_msg = "invalid literal for int() with base 10:"
        assert error_msg in str(e.value)

def test_getter_name(raw_item):
    item = Item(**raw_item)
    assert item.name == 'banana'

def test_getter_name_equals_to_private_variable_name(raw_item):
    item = Item(**raw_item)
    assert item.name == item._name

def test_getter_code(raw_item):
    item = Item(**raw_item)
    assert item.code == 1

def test_getter_code_equals_to_private_variable_code(raw_item):
    item = Item(**raw_item)
    assert item.code == item._code

def test_getter_price(raw_item):
    item = Item(**raw_item)
    assert item.price == 1.1

def test_getter_price_equals_to_private_variable_code(raw_item):
    item = Item(**raw_item)
    assert id(item.price) == id(item._price)

def test_repr_method_return_shaded_attributes(raw_item):
    item = Item(**raw_item)
    result = item.__repr__()
    expected = 'Item(name=banana, code=1, price=1.10)'
    assert result == expected 


