# Test Driven Development_Kata
For this Kata I practiced Test Driven Development by completed another FizzBuzz example.

## Things you need:
- PyTest 3.7 or higher
- Python 5.4.1 or higher

## Testing Notes:
1. Red, Green, Refactor
2. Write the tests in test_fizzbuzz.py and the 'production' code in fizzbuzz.py
3. It is ideal to write the smallest amount of code you can to make the test pass.
4. The names of the tests should also be named as testing functionality (ex.'test_fizz') never 'divisible_by_three'. 

## Refactoring
Even though we refactored while we were writing the coding, this program can be refactored a little more by taking the calculations out of fizzbuzz and putting them in a 'helpers.py' file.

In this file you would have functions/modules like is_fizzbuzz(),is_fizz(), is_buzz()

- These functions would have the conditionals 
```python
if (num % 3 == 0) and (num % 5 == 0):
        result = 'FizzBuzz'
    elif num % 3 == 0:
        result = 'Fizz'
    elif num % 5 == 0:
        result = 'Buzz'
```
- This will allow for the logic to be hidden in the fizzbuzz.py file and it will just import the is_fizzbuzz(),isfizz(),isbuzz() modules from the helpers.py file.
