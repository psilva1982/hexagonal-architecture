from abc import ABC, abstractmethod
from uuid import uuid4

ENABLE="enabled"
DISABLE="disabled"

class ProductInterface(ABC):
    
    def __init__(self, id: str, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price
        self.status = ENABLE if price > 0 else DISABLE

    @abstractmethod
    def is_valid() -> bool:
        pass
    
    @abstractmethod
    def enable():
        pass

    @abstractmethod
    def disable():
        pass

    @abstractmethod
    def get_name() -> str:
        pass

    @abstractmethod
    def get_id() -> str:
        pass

    @abstractmethod
    def get_price() -> float:
        pass
    
    @abstractmethod
    def get_status() -> str:
        pass