fibonacci = [1, 2]
number = len(fibonacci)
while number < 100:
    fibonacci.append(fibonacci[number - 2] + fibonacci[number - 1])
    number = number + 1
fibonacci