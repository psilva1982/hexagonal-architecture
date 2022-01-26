
from os import name
from app.interface import ProductInterface
from app.product import Product
from app.services.interface import ProductPersistenceInterface
from decouple import config
from deta import Deta
from typing import Optional

class ProductDb(ProductPersistenceInterface):

    def __init__(self):
        project_key = config('DB_KEY')
        deta = Deta(project_key)
        self.products = deta.Base("products")

    def get_all(self) -> list:

        fetch_res = self.products.fetch({})
        products = []
        for item in fetch_res.items:
            products.append(item)

        return products

    def get(self, id: str) -> Optional[ProductInterface]:
        fetch_res = self.products.fetch({"id": id})
        if fetch_res.count > 0:
            fetch = fetch_res.items[0]
            product = Product(
                id=fetch['id'],
                name=fetch['name'],
                price=fetch['price']
            )

            return product

        return None

    def get_by_name(self, name: str) -> Optional[ProductInterface]:
                
        fetch_res = self.products.fetch({"name": name})
        if fetch_res.count > 0:
            fetch = fetch_res.items[0]
            product = Product(
                id=fetch['id'],
                name=fetch['name'],
                price=fetch['price']
            )

            return product
        
        return None

    def __create__(self, product: ProductInterface) -> ProductInterface:
        self.products.insert({
           "id": product.get_id(),
           "name": product.name,
           "price": product.price,
           "status": product.get_status()
        })

        return product

    def save(self, product: ProductInterface) -> ProductInterface:
        
        fetch_res = self.products.fetch({"name": product.name})
        if fetch_res.count > 0: 
            item = fetch_res.items[0]
            self.products.update({
                "name": product.name,
                "price": product.price                
            }, item['key'])

        else:
            return self.__create__(product=product)