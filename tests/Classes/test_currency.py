import pytest

from shoppingcart.classes.Currency import Currency
from shoppingcart.custom_exceptions.CurrencyAvailability import CurrencyNotAvailable

def test_currency_object_instantiation(new_currency):
    c = new_currency
    assert isinstance(c, Currency)

def test_currency_object_fail_instantiation():
    with pytest.raises(TypeError) as e:
        c = Currency()
        assert str(e.value) == 'Currency.__init__() missing 1 required positional argument: \'currency\''

def test_get_exchange_rate(new_currency):
    c = new_currency
    result = c.get_exchange_rate()
    expected = {'iso': 'R$', 'rate': 5.4}
    assert result == expected

def test_get_exchange_rate_throws_an_error():
    with pytest.raises(CurrencyNotAvailable) as e:
        c = Currency('EUR')
        c.get_exchange_rate()

def test_get_exchange_rate_throws_error_message():
    with pytest.raises(CurrencyNotAvailable) as e:
        c = Currency('EUR')
        c.get_exchange_rate()
        assert str(e.value) == 'Not allowed to convert to that currency'