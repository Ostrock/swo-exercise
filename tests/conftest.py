import pytest

from shoppingcart.classes.Currency import Currency
from shoppingcart.classes.Item import Item
from shoppingcart.classes.Sale import Sale

@pytest.fixture
def banana():
    return "banana - 2 - €1.10"

@pytest.fixture
def kiwi():
    return "kiwi - 3 - €3.00"

@pytest.fixture
def apple():
    return "apple - 1 - €2.00"

@pytest.fixture
def new_currency():
    c = Currency('BRL')
    return c

@pytest.fixture
def raw_item():
    item = {
        '_name': 'banana',
        '_code': 1,
        '_price': 1.10
    }
    return item

@pytest.fixture
def raw_sale():
    item = {
        '_name': 'banana',
        '_code': 1,
        '_price': 1.10
    }
    s = Sale(Item(**item), 1)
    return s

@pytest.fixture
def raw_sale_more_than_one():
    item = {
        '_name': 'banana',
        '_code': 1,
        '_price': 1.10
    }
    s = Sale(Item(**item), 2)
    return s