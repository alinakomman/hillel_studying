def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_numbers(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            yield num


start = 10
end = 90

prime_list = list(prime_numbers(start, end))

print(f"Found next prime numbers from the range {{{start}:{end}}}:")
for i in range(len(prime_list)):
    print(prime_list[i], end="" if i == len(prime_list) - 1 else ", ")
