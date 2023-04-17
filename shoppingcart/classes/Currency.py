from dataclasses import dataclass

from shoppingcart.custom_exceptions.CurrencyAvailability import CurrencyNotAvailable

@dataclass
class Currency:
    currency: str

    def get_exchange_rate(self):
        currencies = {
            'BRL': {'iso': 'R$', 'rate': 5.4},
            'USD': {'iso': '$', 'rate': 1.1},
            'GBP': {'iso': '£', 'rate': 0.89}
            }
        
        if currencies.get(self.currency) is not None:
            return currencies.get(self.currency)
        else:
            raise CurrencyNotAvailable('Not allowed to convert to that currency')
