
from app.product import Product
from app.services.interface import ProductPersistenceInterface, ProductServiceInterface
from app.interface import ProductInterface
import uuid
from typing import Optional

class ProductService(ProductServiceInterface):

    def __init__(self, persistence: ProductPersistenceInterface):
        self.__persistence = persistence
    
    def get(self, id: str) -> Optional[ProductInterface]:
        return self.__persistence.get(id=id)

    def get_by_name(self, name: str) -> Optional[ProductInterface]:
        return self.__persistence.get_by_name(name=name)

    def get_all(self) -> list:
        return self.__persistence.get_all()

    def create(self, name: str, price: float) -> ProductInterface:
        product = Product(id=uuid.uuid4(), name=name, price=price) 
        return self.__persistence.save(product=product)

    def enable(self, product: ProductInterface) -> ProductInterface:
        product.enable()
        return self.__persistence.save(product=product)

    def disable(self, product: ProductInterface) -> ProductInterface:
        product.disable()
        return self.__persistence.save(product=product)