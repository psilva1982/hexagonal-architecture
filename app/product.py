from pickle import TRUE
from tkinter import N
from tkinter.messagebox import NO
from uuid import uuid4
from .interface import ProductInterface
from .interface import ENABLE, DISABLE
from app import exceptions

class Product(ProductInterface):

    def is_valid(self) -> bool:
        if self._ProductInterface__status == None:
            self._ProductInterface__status = DISABLE
        
        if self._ProductInterface__status != ENABLE and self._ProductInterface__status != DISABLE:
            raise exceptions.ProductStatusError
        
        if self.price < 0 and self._ProductInterface__status == ENABLE:
            raise exceptions.ProductEnableError

        return True

    def enable(self):
        if self.price > 0: 
            self.__status = ENABLE

        else: 
            raise exceptions.ProductEnableError

    def disable(self):
        if self.price <= 0: 
           self.__status = DISABLE

        else: 
            raise exceptions.ProductDisableError

    def get_name(self) -> str:
        return self.name

    def get_id(self) -> str:
        return self._ProductInterface__id

    def get_price(self) -> float:
        return self.price
    
    def get_status(self) -> str:
        return self._ProductInterface__status