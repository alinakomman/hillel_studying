# 1
string = input("Enter a string:")
unique_symbols_count = len(set(string))

if unique_symbols_count > 10:
    print(True)
else:
    print(False)

# 2
string = input("Enter a string:")
unique_symbols_count = sum(string.count(char) == 1 for char in string)

if unique_symbols_count > 10:
    print(True)
else:
    print(False)
