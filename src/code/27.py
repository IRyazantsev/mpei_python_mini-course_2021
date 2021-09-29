def calc_factorial(num):
    factorial = 1
    if  num >= 0:
        for i in range(1, num + 1):
            factorial = i * factorial
        return factorial

factorial = calc_factorial(5)
print(factorial)
