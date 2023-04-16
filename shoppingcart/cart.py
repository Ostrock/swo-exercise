from typing import List, Dict

from shoppingcart import abc as abs
from shoppingcart.classes.Sale import Sale
from shoppingcart.classes.Item import Item


class ShoppingCart(abs.ShoppingCart):
    def __init__(self):
        self._items: List[Sale] = []
        self._processed_items: Dict[int, int] = {}

    def add_item(self, product_code: str, quantity: int) -> None:
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
        total = 0
        for item in self._items:
            lines.append(str(item))
            total += item.total_price
        lines.append(' ')
        lines.append(f'Total: {total:.2f}')
        return lines

    def _get_product_price(self, product_code: str) -> float:
        products = {
            1: {'_name':'apple', '_price': 1.0},
            2: {'_name':'banana', '_price': 1.1},
            3: {'_name':'kiwi', '_price': 3.0}
        }

        if products.get(product_code) is not None:
            price = {'_code': product_code} | products[product_code]
            return price
        
