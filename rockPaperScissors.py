#A simple Rock, Paper, Scissors game. Practicing flow control statements
from random import*

#Set computer choice
computer = randint(1,3)
if computer == 1:
    computer = 'Rock'
elif computer == 2:
    computer = 'Paper'
elif computer == 3:
    computer = 'Scissors'

#Player choice
print('Rock, Paper or Scissors?')
player = raw_input()

#Print each outcome
if player == 'Rock' or player == 'r' or player == 'rock':
    if computer == 'Rock':
        print(computer)
        print('It was a draw!')
    elif computer == 'Paper':
        print(computer)
        print('Computer wins!')
    elif computer == 'Scissors':
        print(computer)
        print('You win!')

elif player == 'Paper' or player == 'p' or player == 'paper':
    if computer == 'Rock':
        print(computer)
        print('You win!')
    elif computer == 'Paper':
        print(computer)
        print('It was a draw!')
    elif computer == 'Scissors':
        print(computer)
        print('Computer wins!')

elif player == 'Scissors' or player == 's' or player == 'scissors':
    if computer == 'Rock':
        print(computer)
        print('Computer wins!')
    elif computer == 'Paper':
        print(computer)
        print('You win!')
    elif computer == 'Scissors':
        print(computer)
        print('It was a draw!')