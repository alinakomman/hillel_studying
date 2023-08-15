def generator(first, second):
    certain_number = first
    while certain_number <= second:
        yield certain_number
        certain_number += 1


for num in generator(3, 33):
    print(num)
