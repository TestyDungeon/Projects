def factorial(number):
    if number > 1:
        result = number * factorial(number - 1)
        return result
    elif number == 1:
        return 1

print(factorial(9))