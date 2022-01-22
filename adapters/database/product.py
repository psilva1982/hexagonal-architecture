
from math import prod
from application.interface import ProductInterface
from application.product import Product
from application.services.interface import ProductPersistenceInterface
from decouple import config
from deta import Deta


class ProductDb(ProductPersistenceInterface):

    def __init__(self) -> None:
        project_key = config('DB_KEY')
        deta = Deta(project_key)
        self.products = deta.Base("users")

    def get(self, id: str) -> ProductInterface:
        fetch_res = self.products.fetch({"id": id})
        fetch = fetch_res.items[0]
        product = Product(
            id=fetch['id'],
            name=fetch['name'],
            price=fetch['price'],
            status=fetch['status']
        )

        return product

    def save(self, product: ProductInterface)-> ProductInterface:
        self.products.insert({
           "id": str(product.id),
           "name": product.name,
           "price": product.price,
           "status": product.status
        })

        return product
