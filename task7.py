# write a new list with even numbers


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

evenNumbers = []

for number in a:
    if number % 2 == 0:
        evenNumbers.append(number)

print(evenNumbers)


# list comprehension

newListWithEvenNumbers = [element for element in a if element % 2 == 0]

print(newListWithEvenNumbers)
