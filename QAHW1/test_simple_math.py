import pytest
from simple_math import SimpleMath

@pytest.fixture
def simple_math_test():
    return SimpleMath()

#Square tests
def test_square_positive(simple_math_test):
    assert simple_math_test.square(103233) == 103233 ** 2

def test_square_negative(simple_math_test):
    assert simple_math_test.square(-111) == -111 ** 2

def test_square_null(simple_math_test):
    assert simple_math_test.square(0) == 0


#Cube tests
def test_cube_positive(simple_math_test):
    assert simple_math_test.cube(103233) == 103233 ** 3

def test_cube_negative(simple_math_test):
    assert simple_math_test.cube(-111) == -111 ** 3

def test_cube_null(simple_math_test):
    assert simple_math_test.cube(0) == 0