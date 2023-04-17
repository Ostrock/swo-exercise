from dataclasses import dataclass

@dataclass
class Item:
    _name: str
    _code: int
    _price: float

    @classmethod
    def code_validator(cls, code:str) -> int:
        try:
            code_trim = code.strip()
            code_int = int(code_trim)
            return code_int
        except Exception as e:
            print(str(e))
        
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def code(self) -> int:
        return self._code
    
    @property
    def price(self) -> float:
        return self._price
    
    def __repr__(self) -> str:
        return f'Item(name={self.name}, code={self.code}, price={self.price:.2f})'
    
    