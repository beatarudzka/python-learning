#rock, paper, scissors
import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input(
    "%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input(
    "%s, do you want to choose rock, paper or scissors?" % user2)


def game(u1, u2):
    if u1 == u2:
        print("Draw")
    elif u1 == 'rock':
        if u2 == 'scissors':
            print('Rock wins')
        else:
            print('Paper wins')
    elif u1 == 'scissors':
        if u2 == 'paper':
            print('Scissors win')
        else:
            print('Rock wins')
    elif u1 == 'paper':
        if u2 == 'rock':
            print('Paper wins')
        else:
            print('Scissors wins')
    else:
        return("Invalid input: you have to choose between rock, paper and scissors")


print(game(user1_answer, user2_answer))
