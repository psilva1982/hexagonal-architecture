
from math import prod
from tkinter.messagebox import NO
from app.interface import ProductInterface
from app.product import Product
from app.services.interface import ProductPersistenceInterface
from decouple import config
from deta import Deta
from typing import Optional

class ProductDb(ProductPersistenceInterface):

    def __init__(self) -> None:
        project_key = config('DB_KEY')
        deta = Deta(project_key)
        self.products = deta.Base("products")

    def get(self, id: str) -> Optional[ProductInterface]:
        try:
            fetch_res = self.products.fetch({"id": id})
            if len(fetch_res.items) > 0:
                fetch = fetch_res.items[0]
                product = Product(
                    id=fetch['id'],
                    name=fetch['name'],
                    price=fetch['price']
                )

                return product
        except: 
            return None
        
        return None

    def get_by_name(self, name: str) -> Optional[ProductInterface]:
                
        fetch_res = self.products.fetch({"name": name})
        if len(fetch_res.items) > 0:
            fetch = fetch_res.items[0]
            product = Product(
                id=fetch['id'],
                name=fetch['name'],
                price=fetch['price']
            )

            return product
        
        return None

    def save(self, product: ProductInterface)-> ProductInterface:
        self.products.insert({
           "id": str(product.get_id()),
           "name": product.name,
           "price": product.price,
           "status": product.get_status()
        })

        return product
