import random

a = range(1, random.randint(1, 30))
b = range(1, random.randint(10, 40))

listWithTheSameNumbers = []

for numbers in a:
    if numbers in b and numbers not in listWithTheSameNumbers:
        listWithTheSameNumbers.append(numbers)

print(a, b, listWithTheSameNumbers)
