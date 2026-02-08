
'''
choices = ['rock', 'paper', 'scissors']


computer_choice = random.choice(choices) 

 
try:    
    print (f'you chose {user_choice} \nthe computer chose {computer_choice}') 
except:
    print('an error occured please try again')
        

    
def win():
    while True:
        user_choice = input('Choose (rock paper or scissors) - ')
        
       # user_choice.strip().lower()

        if user_choice == 'rock' and computer_choice =='paper':
            print ('the computer wins\n there is still a next round😃')   
    
        elif user_choice == 'paper' and computer_choice == 'scissors':
            print ('the computer wins\n there is still a next round😃')   
        
        elif user_choice == 'scissors' and computer_choice == 'rock':
            print ('the computer wins\n there is still a next round😃')   
        
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print('yeah you did it, you win✅🌟')
     
        elif user_choice == 'paper' and computer_choice == 'scissors':
            print('yeah you did it, you win✅🌟')
    
        elif user_choice == 'paper' and computer_choice == 'rock': 
            print('yeah you did it, you win✅🌟')
 
        elif user_choice == computer_choice:
            print('try again, there is no draw')
     
        else:
            print('invalid input \nthe only accepted inputs are:'.upper() + '\nrock\npaper\nscissors \n\n\n')
        
       

win()

'''

'''
let us play rock paper scissors

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
        
    