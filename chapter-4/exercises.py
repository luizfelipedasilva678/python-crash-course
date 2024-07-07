# for value in range(1, 21):
# print(value)

# for value in range(1, 1_000_001):
#   print(value)


numbers = list(range(1, 1_000_001))

print(f"Result {sum(numbers)}")

odd_numbers = [value for value in range(-1, 20, 2)]

print(odd_numbers)


threes = [value * 3 for value in range(1, 11)]

print(threes)

cubes = [value**3 for value in range(1, 11)]

print(cubes)
