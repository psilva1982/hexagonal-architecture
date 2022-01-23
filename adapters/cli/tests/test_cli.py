from math import prod
from unicodedata import name
import unittest
from adapters.cli import product as cli
from app.interface import ProductInterface
from app.product import Product
from app.services.interface import ProductServiceInterface
import uuid 
from app.interface import ENABLE
from unittest.mock import MagicMock

class TestCli(unittest.TestCase):

    def setUp(self):
        self.id = uuid.uuid4()
        self.mock = ProductInterface
        self.product = Product(id=self.id, name="Product", price=10)

    def test_cli(self):
        self.mock.get_id = MagicMock(return_value=self.id)
        self.mock.get_status = MagicMock(return_value=self.product.get_status())
        self.mock.price = MagicMock(return_value=self.product.price)
        self.mock.name = MagicMock(return_value=self.product.name)
        
        service = ProductServiceInterface
        service.create = MagicMock(return_value=self.mock)
        service.get = MagicMock(return_value=self.mock)
        service.enable = MagicMock(return_value=self.mock) 
        service.disable = MagicMock(return_value=self.mock)

        resultExpected = f'Product ID {self.mock.get_id()} with the name {self.mock.name} has been created with the price {self.mock.price} and status {self.mock.get_status()}'
        result = cli.run(service=service, action="create", product_id="", name=self.product.name, price=self.product.price)
        
        assert resultExpected == result
