import pytest

from conftest import base_price


class Calculator:
    def __init__(self,count=0):
        self.__count = count


    def add(self,x,y):
        return x+y

    def calculate_discount(self,price,discount_percent):
        if(price < 0 or discount_percent < 0):
            raise ValueError("Price and discount must be non-negative.")
        return ((100-discount_percent)/100)*price