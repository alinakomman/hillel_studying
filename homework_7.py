data = {
    'good': 580,
    'tanks': 16,
    'vehicle': 13,
    'artillery': 15,
    'aircraft': 1,
    'UAV': 4,
    'other': 20
}

file_name = 'vtraty_rosiyan_za_10_08.txt'

with open(file_name, 'w') as file:
    for key, value in data.items():
        file.write(f'{key}: {value}\n')


def calculate_sum(file_name):
    try:
        with open(file_name, 'r') as file:
            values = [int(line.split(': ')[1]) for line in file]
            return sum(values)
    except (FileNotFoundError, ValueError, IndexError):
        pass

amount = calculate_sum(file_name)
print(f'{file_name}: {amount}')
