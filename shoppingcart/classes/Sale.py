from dataclasses import dataclass

from shoppingcart.classes.Item import Item
from shoppingcart.utils.logger import shopping_cart_logger

@dataclass 
class Sale:
    _item: Item
    _quantity: int = 1
    _total_price: float = 1.0

    def __post_init__(self):
        try:
           if self.validate_quantity(self._quantity):
            self._total_price = self._item.price * self._quantity   
        except Exception as e:
            print(str(e))

    @property
    def item(self) -> Item:
        return self._item
    
    @property
    def quantity(self) -> int:
        return self._quantity
    
    @quantity.setter
    def quantity(self, quantity: int) -> None:
        try:
            if self.validate_quantity(quantity):
                self._quantity = quantity
        
        except Exception as e:
            print(str(e))

    @property
    def total_price(self) -> float:
        return self._total_price
    
    def calc_total_price(self, quantity):
        self._total_price = quantity * self.item.price
        

    @classmethod
    def validate_quantity(cls, number: int) -> bool:
        if number < 1:
            raise ValueError('The quantity of a product been sold should be greater than 0 or less')
        else:
            return True
        
    def __str__(self) -> str:
        return f'{self.item.name} - {self.quantity} - €{self.total_price:.2f}'
    
    def __repr__(self):
        return f'Sale({str(self.item)}, quantity={self.quantity}, total_price={self.total_price:.2f})' 