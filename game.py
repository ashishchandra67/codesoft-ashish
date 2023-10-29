# A game of stone paper scissor with user input

import random
while True:
    user_score = 0 
    
    possible_actions = ['stone' , 'paper' , 'scissor']
    user = input("enter your choice\n1.Stone\n2.paper\n3.scissors\n")
    computer = random.choice(possible_actions)

    print(f"You choose: {user} and computer choose:{computer} \n")

    if user == computer:
       print(f"You choose: {user} and computer choose:{computer} \n")
       print("The match is draw!!")
    
    if user == 'stone':
        if computer =='scissors':
            print(f"You win with stone against scissors")
            user_score+=1
        else:
            print(f"computer wins with stone against scissors")

    elif user == 'paper':
        if computer =='scissors':
            print(f"Computer wins with paper against paper")
        else:
            print(f"You win with stone against paper ")
            user_score+=1
    
    elif user == 'scissor':
        if computer =='paper':
            print(f"you  wins with scissor against paper")
            user_score+=1
        else:
            print(f"computer win with stone against paper ")
            
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    
print("The resultt after the gameee is : ", user_score)
    


