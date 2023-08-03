def arguments(arg1, arg2):
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        return arg1 * arg2
    elif isinstance(arg1, str) and isinstance(arg2, str):
        return arg1 + arg2
    else:
        return arg1, arg2


dead_russians = arguments(70000000, 2)
gaslo = arguments('Slava', ' Ukraini!')
supply = arguments('F-', 16)

print(dead_russians)
print(gaslo)
print(supply)
