print("=" * 40 + " Task 1 " + 40 * "=")
message = "You have to enter a word with 'o', please, "

while True:
    word = input("Enter a word:")
    if "o" in word.lower():
        print("Niiice!")
        break
    else:
        print(message)


print("=" * 40 + " Task 2 " + 40 * "=")
list_1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list_2 = []

for item in list_1:
    if isinstance(item, str):
        list_2.append(item)

print(list_2)


print("=" * 40 + " Task 3 " + 40 * "=")
list = [24, 9, 88, 6, 5, 7, 2, 45, 99, 13, 3, 2, 134]
sum_of_even_numbers = 0
even_numbers = []

for num in list:
    if num % 2 == 0:
        sum_of_even_numbers += num
        even_numbers.append(num)

print("Even numbers:", even_numbers)
print("Sum of all even numbers:", sum_of_even_numbers)