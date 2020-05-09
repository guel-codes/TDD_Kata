def fizzbuzz(num):
    result = ''
    if (num % 3 == 0) and (num % 5 == 0):
        result = 'FizzBuzz'
    elif num % 3 == 0:
        result = 'Fizz'
    elif num % 5 == 0:
        result = 'Buzz'
    else:
        result = num
    return result

