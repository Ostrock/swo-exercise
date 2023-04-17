from typing import List, Dict
from json import load

from shoppingcart import abc as abs
from shoppingcart.classes.Currency import Currency
from shoppingcart.classes.Item import Item
from shoppingcart.classes.Sale import Sale
from shoppingcart.custom_exceptions.CurrencyAvailability import CurrencyNotAvailable

class ShoppingCart(abs.ShoppingCart):
    def __init__(self):
        self._items: List[Sale] = []
        self._processed_items: Dict[int, int] = {}

    def add_item(self, product_code: str, quantity: int) -> None:
        product_code_int = Item.code_validator(product_code)
        new_item  = Item(**self._get_product_price(product_code_int))
        try:
            if Sale.validate_quantity(quantity):
                self._quantity = quantity
            if self._processed_items.get(new_item.code) is not None:
                index = self._processed_items.get(new_item.code)
                self._items[index].quantity = self._items[index].quantity + quantity
                self._items[index].calc_total_price(self._items[index].quantity)

            elif Sale.validate_quantity(quantity):
                self._quantity = quantity
                sale = Sale(new_item, quantity)
                self._processed_items.setdefault(new_item.code, len(self._processed_items))
                self._items.append(sale)
        except Exception as e:
            print(str(e))


    def print_receipt(self, currency=None, exchange_currency = Currency):
        if currency is not None:
            new_currency = exchange_currency(currency)
            try:
                currency_info = new_currency.get_exchange_rate()
            except CurrencyNotAvailable:
                print("Not allowed to convert to that currency")          
            exchange_rate = currency_info.get('rate')
            currency_iso = currency_info.get('iso')            
            lines = []
            total = 0
            for sold_item in self._items:
                price = sold_item._total_price
                converted_price = (price * exchange_rate)
                total += converted_price
                repr_str = f'{sold_item.item.name} - {sold_item.quantity} - {currency_iso}{converted_price:.2f}'
                lines.append(repr_str)
            lines.append(' ')
            lines.append(f'Total: {total:.2f}')
            return lines
        
        else:
            lines = []
            total = 0
            for item in self._items:
                lines.append(str(item))
                total += item.total_price
            lines.append(' ')
            lines.append(f'Total: {total:.2f}')
            return lines


    def _get_product_price(self, product_code: str) -> float:
        products = self._get_from_json()

        if products.get(product_code) is not None:
            price = {'_code': product_code} | products[product_code]
            return price
    
    def _get_from_json(self):
        try:
            with open('common_prices.json') as f:
                data = load(f)
                adapted = {}
                for k,v in data.items():
                    adapted.setdefault(int(k),v)
            return adapted
        except Exception as e:
            print(str(e))