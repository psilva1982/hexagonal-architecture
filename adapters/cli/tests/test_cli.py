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

        result_expect_create = f'Product ID {self.mock.get_id()} with the name {self.mock.name} has been created with the price {self.mock.price} and status {self.mock.get_status()}'
        result_create = cli.run(service=service, action="create", product_id="", name=self.product.name, price=self.product.price)
        
        result_expected_disable = f"Product ID {self.mock.get_id()} has been disabled"
        result_disable = cli.run(service=service, action="disable", product_id=self.id, name="", price="")

        result_expected_enable = f"Product ID {self.mock.get_id()} has been enabled"
        result_enable = cli.run(service=service, action="enable", product_id=self.id, name="", price="")

        assert result_create == result_expect_create
        assert result_disable == result_expected_disable
        assert result_enable == result_expected_enable
