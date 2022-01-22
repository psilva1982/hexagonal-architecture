from abc import ABC, abstractmethod
from application.interface import ProductInterface

class ProductServiceInterface(ABC):

    @abstractmethod
    def get(id: str) -> ProductInterface:
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


class ProductReader(ABC):

    @abstractmethod
    def get(id: str) -> ProductInterface:
        pass

class ProductWriter(ABC):

    @abstractmethod
    def save(product: ProductInterface) -> ProductInterface:
        pass

class ProductPersistenceInterface(ProductWriter, ProductReader):
    pass