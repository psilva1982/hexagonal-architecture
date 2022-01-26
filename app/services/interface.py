from abc import ABC, abstractmethod
from app.interface import ProductInterface
from typing import Optional

# ServiceInterface
class ProductServiceInterface(ABC):

    @abstractmethod
    def get(id: str) -> ProductInterface:
        pass

    @abstractmethod
    def get_all() -> list:
        pass

    @abstractmethod
    def get_by_name(name: str) -> Optional[ProductInterface]:
        pass

    @abstractmethod
    def create(name: str, price: float) -> ProductInterface:
        pass

    @abstractmethod
    def enable(product: ProductInterface) -> ProductInterface:
        pass

    @abstractmethod
    def disable(product: ProductInterface) -> ProductInterface:
        pass


# PersistenseInterfaces
class ProductReader(ABC):

    @abstractmethod
    def get(id: str) -> Optional[ProductInterface]:
        pass

    @abstractmethod
    def get_by_name(name: str) -> Optional[ProductInterface]:
        pass

    @abstractmethod
    def get_all() -> list:
        pass

class ProductWriter(ABC):

    @abstractmethod
    def save(product: ProductInterface) -> ProductInterface:
        pass

class ProductPersistenceInterface(ProductWriter, ProductReader):
    pass