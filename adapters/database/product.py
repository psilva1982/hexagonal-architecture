
from application.interface import ProductInterface
from application.services.interface import ProductPersistenceInterface


class ProductDb(ProductPersistenceInterface):

    def __init__(self) -> None:
        self.project_key = 'b0566nxt_qR5eySrD4j5uzj5BrAubX1srd5PG6Ss3'
        self.project_id = ''

    def get(self, id: str) -> ProductInterface:
        pass

    def save(self, product: ProductInterface):
        pass
