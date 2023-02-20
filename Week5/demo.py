import pytest
from unittest.mock import patch

def test_upper():
    with patch("builtin_inputs", return_value="Tim")
    assert make_upper() == "TIM"

def make_upper():
    value = input("Enter name?")
    return value.upper()


# @pytest.fixture
# def tim():
#     p = Person("Tim")
#     return p

# def test_init(tim):
#     p = Person("Tim")
#     assert tim.name == "Tim"

# def test_upper(tim):
#     tim.name = "bob"
#     assert p.upper == "BOB"

# class Person:
#     def __init__(self,name) -> None:
#         self.name = name

#     def upper(self):
#         return self.name.upper()