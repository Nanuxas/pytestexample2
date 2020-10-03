class Calculator:
    def sudetis(self, a, b):
        return a + b

    def atimtis(self, a, b):
        return a - b

    def dalyba(self, a, b):
        if a == 0:
            return "Blogai"
        else:
            return a / b

    def daugyba(self, a, b):
        return a * b

    def laipsnis(self, a, b):
        return a ** b

import pytest

def test_sudetis():
    calculator = Calculator()
    assert calculator.sudetis(1, 2) == 3

def test_sudetis1():
    calculator = Calculator()
    with pytest.raises(Exception):
        assert calculator.sudetis("trys", 2)

def test_atimtis():
    calculator = Calculator()
    assert calculator.atimtis(2, 2) == 0

def test_dalyba():
    calculator = Calculator()
    assert calculator.dalyba(0, 0) == "Blogai"

def test_daugyba():
    calculator = Calculator()
    assert calculator.daugyba(-2, 3) == -6

def test_laipsnis():
    calculator = Calculator()
    assert calculator.laipsnis(1, 100) == 1



