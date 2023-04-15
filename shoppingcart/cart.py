from typing import List, Dict

from shoppingcart import abc as abs
from shoppingcart.classes.Sale import Sale
from shoppingcart.classes.Item import Item


class ShoppingCart(abs.ShoppingCart):
    def __init__(self):
        self._items: List[Sale] = []
        self._processed_items: Dict[int, int] = {}

    def add_item(self, product_code: str, quantity: int):
        product_code_int = Item.code_validator(product_code)
        new_item  = Item(**self._get_product(product_code_int))
        try:
            if self._processed_items.get(new_item.code) is not None:
                index = self._processed_items.get(new_item.code)
                add = Sale.validate_quantity(quantity)
                self._items[index].quantity = self._items[index].quantity + add
                self._items[index].total_price = self._items[index].price * self._items[index].quantity

            else:
                quantity = Sale.validate_quantity(quantity)
                sale = Sale(new_item, quantity)
                self._processed_items.setdefault(new_item.code, len(self._processed_items))
                self._items.append(sale)
        except Exception as e:
            print(str(e))

    def print_receipt(self) -> List[str]:
        lines = []

        for item in self._items.items():
            price = self._get_product_price(item[0]) * item[1]

            price_string = "€%.2f" % price

            lines.append(item[0] + " - " + str(item[1]) + ' - ' + price_string)

        return lines

    def _get_product_price(self, product_code: str) -> float:
        price = 0.0

        if product_code == 'apple':
            price = 1.0

        elif product_code == 'banana':
            price = 1.1

        elif product_code == 'kiwi':
            price = 3.0

        return price
