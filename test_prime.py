from prime_factors import  *

def test_find_prime_factors():
    assert find_prime_factors(0) == []
    assert find_prime_factors(1) == []
    assert find_prime_factors(2) == [2]
    assert find_prime_factors(3) == [3]
    assert find_prime_factors(4) == [2,2]
    assert find_prime_factors(5) == [5]
    assert find_prime_factors(6) == [2,3]
    assert find_prime_factors(7) == [7]
    assert find_prime_factors(8) == [2,2,2]
    assert find_prime_factors(9) == [3,3]
    assert find_prime_factors(10) == [2,5]
 


def test_find_prime_factors_2():
    assert find_prime_factors_2(0) == []
    assert find_prime_factors_2(1) == []
    assert find_prime_factors_2(2) == [2]
    assert find_prime_factors_2(3) == [3]
    assert find_prime_factors_2(4) == [2,2]
    assert find_prime_factors_2(5) == [5]
    assert find_prime_factors_2(6) == [2,3]
    assert find_prime_factors_2(7) == [7]
    assert find_prime_factors_2(8) == [2,2,2]
    assert find_prime_factors_2(9) == [3,3]
    assert find_prime_factors_2(10) == [2,5]
