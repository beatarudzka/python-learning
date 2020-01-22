# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


numberToCheck = int(input('Write your number to divide: '))

listOfPossibleDivisors = list(range(1, numberToCheck + 1))

divisorList = []

for number in listOfPossibleDivisors:
    if numberToCheck % number == 0:
        divisorList.append(number)

print(divisorList)
