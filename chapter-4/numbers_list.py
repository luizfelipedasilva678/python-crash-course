from math import pow

for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))

even_numbers = list(range(2, 11, 2))

print(even_numbers)

squares = []

for value in range(1, 11):
    square = pow(value, 2)
    squares.append(square)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(min(digits))

squares = [value**2 for value in range(1, 11)]

print(squares)
