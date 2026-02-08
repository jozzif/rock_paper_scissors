'''
rock paper scissors where you choose between rock, paper and scissors then the computer programme chooses and the algorithm determines the winner

'''

import random


choices = ['rock', 'paper', 'scissors']


rules ={
    'scissors':'paper',
    'rock': 'scissors',
    'paper':'rock'    
}

while True:
    user_choice = input("Choose rock, paper or scissors: ").strip().lower()

    computer_choice = random.choice(choices)

    print(f"You chose {user_choice}, computer chose {computer_choice}")

    if user_choice not in choices:
        print('invalid')
    elif user_choice == computer_choice:
        print('draw')
    elif rules[user_choice] == computer_choice:
        print('user wins')
    else:
        print('computer wins')
    
        
    option = input('do you want to quit (y for yes and n for no) ').strip().lower()
    
    if option == 'n':
        continue
         
    elif option == 'y':
        break
    else:
        print('invalid choice')
        

    
