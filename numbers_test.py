import assignment_numbers

def test_sum():
    assert assignment_numbers.get_sum(1, 2) == 3

def test_difference():
    assert assignment_numbers.get_difference(3, 2) == 1

def test_product():
    assert assignment_numbers.get_product(2, 3) == 6

def test_float_quotient():
    assert assignment_numbers.get_float_quotient(1, 2) == 0.5

def test_floored_quotient():
    assert assignment_numbers.get_floored_quotient(3, 2) == 1

def test_remainder():
    assert assignment_numbers.get_remainder(3, 2) == 1

def test_power():
    assert assignment_numbers.get_power(3, 2) == 9