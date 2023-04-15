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
        except Exception as e:
            print(str(e))

        return code_int
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def code(self) -> int:
        return self._code
    
    @property
    def price(self) -> float:
        return self._price
    
    