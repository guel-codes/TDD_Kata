from fizzbuzz import fizzbuzz



def test_number():
    assert fizzbuzz(1) == 1

def test_fizz():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(9) == 'Fizz'
def test_buzz():
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(10) == 'Buzz'

def test_fizz_buzz():
    assert fizzbuzz(15) == 'FizzBuzz'