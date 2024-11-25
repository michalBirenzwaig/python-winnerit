import pytest

from conftest import base_price
from source.calculator import Calculator

test_data=[(3,4,7),(-2,-4,-6)]
@pytest.mark.parametrize("x,y,result",test_data)
def test_calculator(x,y,result):
    calc = Calculator()
    assert calc.add(x,y)==result

test_data=[(50,50),(20,80)]
@pytest.mark.parametrize("discount_percent,expected",test_data)
def test_discount(base_price,discount_percent,expected):
    calc = Calculator()
    assert calc.calculate_discount(base_price,discount_percent)==expected


