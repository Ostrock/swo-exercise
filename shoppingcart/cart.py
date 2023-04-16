from typing import List, Dict
from json import load

from shoppingcart import abc as abs
from shoppingcart.classes.Sale import Sale
from shoppingcart.classes.Item import Item


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

    def print_receipt(self) -> List[str]:
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
        with open('common_prices.json') as f:
            data = load(f)
            adapted = {}
            for k,v in data.items():
                adapted.setdefault(int(k),v)
        return adapted