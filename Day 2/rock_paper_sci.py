# rock paper scissors
# create a list of rock paper scissors
# use random choice
import random 

roc_pap_sci = ["rock","paper","scissors"]

def playin_with_bot():
    user_inp=input("\n\n choose your choice from \n rock\n paper\n scissors\n\n ")
    print("Your choice = ",user_inp,"\n ")
    comp_choice = random.choice(roc_pap_sci)
    print("computer choice = ",comp_choice,"\n ")
    if user_inp == comp_choice :
        print("match is draw !!!")
        
    elif user_inp == "rock" and comp_choice == "paper":
        print("BOT Won the game ")
        
    elif user_inp == "rock" and comp_choice == "scissors":
        print("You Won the game ")
        
    elif user_inp == "scissors" and comp_choice == "paper":
        print("You Won the game ")
        
    elif user_inp == "scissors" and comp_choice == "rock":
        print("BOT Won the game ")
        
    elif user_inp == "paper" and comp_choice == "rock":
        print("You Won the game ")
        
    elif user_inp == "paper" and comp_choice == "scissors":
        print("BOT Won the game ")
    return playin_with_bot()

playin_with_bot()        