#TASK 4
#ROCK PAPER SCISSOR GAME


import random

print("----------------WELCOME!---------------")

while(True):
        
    user_choice = input("Enter your choice('rock', 'paper', 'scissor'): ")

    comp_choice = random.choice(['rock', 'paper', 'scissor'])
    
    if user_choice in ['rock', 'paper', 'scissor']:
        if user_choice == comp_choice:
            print("Your Choice: ", user_choice)
            print("Comp's Choice: ", comp_choice)
            print('***************')
            print("---> IT'S DRAW!")
            print('***************\n')

            
        elif ((user_choice=='rock' and comp_choice=='paper') or (user_choice=='paper' and comp_choice=='scissor') or (user_choice=='scissor' and comp_choice=='rock')):
            print("Your Choice:", user_choice)
            print("Comp's Choice:", comp_choice)
            print('***************')
            print('---> YOU LOSE!')
            print('***************\n')
        else:
            print("Your Choice:", user_choice)
            print("Comp's Choice:", comp_choice)
            print('***************')
            print('---> YOU WON!')
            print('***************\n')

    else:
        print('INVALID INPUT!\nTry Again!\n')

    choice = input('DO YOU WANT TO PLAY AGAIN(Y/N)? ')
    if(choice=='N'):        
        print("Quitting...")
        break

