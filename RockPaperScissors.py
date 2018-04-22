'''
import time
import random

magic_choice = random.randint(0, 2)

print("This is a Rock:Paper:Scissors Simulation")
Regular_RPS = ['Rock', 'Paper', 'Scissors']
RPS = ['Rock', 'Paper', 'Scissors', 'rock', 'paper', 'scissors']
print()
time.sleep(.3)
print("Rock!")
time.sleep(0.5)
print("Paper!")
time.sleep(0.5)
print("Scissors!")
time.sleep(0.3)
print("Shoot!")

while True:
    print()
    chooseRPS = input()
    if chooseRPS in RPS:
        break
    else:
        print("Not a valid answer.")
        time.sleep(0.2)

print()
print(chooseRPS.title())
magic_choose = (Regular_RPS[magic_choice])
print(magic_choose)
print()
time.sleep(0.3)
if magic_choose in ['rock'.title()]:
    if chooseRPS in ['Rock'.title()]:
        print("A tie!")
    elif chooseRPS in ['Scissors', 'scissors']:
        print("You lose!")
    elif chooseRPS in ['Paper', 'paper']:
        print("You win!")
elif magic_choose in ['Paper', 'paper']:
    if chooseRPS in ['Paper', 'paper']:
        print("A tie!")
    elif chooseRPS in ['rock'.title()]:
        print("You lose!")
    elif chooseRPS in ['Scissors', 'scissors']:
        print("You win!")
elif magic_choose in ['Scissors', 'scissors']:
    if chooseRPS in ['Scissors', 'scissors']:
        print("A tie!")
    elif chooseRPS in ['rock'.title()]:
        print("You win!")
    elif chooseRPS in ['Paper', 'paper']:
        print("You lose!")

print()
time.sleep(0.2)
print("Thank you for playing :)")
'''

import random

def rps_game():
    magic_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    d = {('Rock','Scissors'): 'You win!', ('Scissors','Paper'): 'You win!',
         ('Paper','Rock'): 'You win!', ('Rock','Rock'): 'Tie',
         ('Scissors','Scissors'): 'Tie', ('Paper','Paper'): 'Tie'}

    player_choice = input('Rock, Paper or Scissors?\n').title()
    print('Magic_choice:', magic_choice)
    print(d.get((player_choice, magic_choice), 'You lose!'))