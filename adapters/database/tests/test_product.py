import unittest
from adapters.database.product import ProductDb
from app.services.product import ProductService
from app.interface import DISABLE

class TestProductDb(unittest.TestCase):

    def setUp(self):
        self.service = ProductService(persistence=ProductDb())
        self.product = self.service.get_by_name(name="Test_Product")

        if self.product is None:
            self.product = self.service.create(name="Test_Product", price=0)

    def test_get_by_name(self):
        product = self.service.get_by_name(name='Test_Product')
        assert product.get_name() == self.product.name
        assert product.get_status() == DISABLE
        assert product.get_price() == 0
    
    def test_create(self):
        product = self.service.create(name="Test create", price=0)
        
