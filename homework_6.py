def fibonacci(a, b):
    if b == 1 and a == 1:
        return [a, b]
    else:
        number = a - b
        return [a] + fibonacci(b, number)

sequence = fibonacci(89, 55)

for num in sequence:
    print(num)
