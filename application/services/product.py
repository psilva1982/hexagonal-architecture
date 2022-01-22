
from application.product import Product
from application.services.interface import ProductPersistenceInterface
from application.interface import ProductInterface
import uuid

class ProductService:

    def __init__(self, persistence: ProductPersistenceInterface):
        self.persistence = persistence
    
    def get(self, id: str) -> ProductInterface:
        return self.persistence.get(id=id)

    def create(self, name: str, price: float) -> ProductInterface:

        product = Product(id=uuid.uuid4(), name=name, price=price) 
        return self.persistence.save(product=product)

    def enable(self, product: ProductInterface) -> ProductInterface:
        product.enable()
        return self.persistence.save(product=product)

    def disable(self, product: ProductInterface) -> ProductInterface:
        product.disable()
        return self.persistence.save(product=product)