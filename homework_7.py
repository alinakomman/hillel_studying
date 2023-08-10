def create_numbers_file(filename):
    numbers = [580, 16, 13, 15, 1, 4, 16, 4]

    with open(filename, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')


filename = 'vtraty_rosiyan_za_10_08.txt'
create_numbers_file(filename)


def calculate_sum_from_file(filename):
    sum = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    sum += number
                except ValueError:
                    pass  
    except FileNotFoundError:
        print(f"File '{filename}' not found")

    return sum


sum_of_numbers = calculate_sum_from_file(filename)
print(f"Summ: '{filename}': {sum_of_numbers}")

