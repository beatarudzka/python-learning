# check if string is palindrom
string = str(input("Write the word:  "))


if string[::] == string[::-1]:
    print("Your word is palindrom")
else:
    print("Your word isn't palindrom")
