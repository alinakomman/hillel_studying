# a
def supply(weapons,amount):
    dead_russians = weapons * amount
    return dead_russians

calculation = supply(70000000, 2)
print(calculation)

# b
def first_gaslo(a,b):
    gaslo = a + b
    return gaslo

say_it = first_gaslo('Slava', ' Ukraini!')
print(say_it)

# c
def second_gaslo(*args):
    return args

say_it = second_gaslo('Heroyam', ' Slava!')
print(say_it)
