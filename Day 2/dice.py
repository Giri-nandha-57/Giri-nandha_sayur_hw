# Two player dice game.
# Each player will roll the die (numbers from 1 to 6)
# points are added to each roll.
# 1 - 1 pt
# 2 - 5 pts
# 3 - 15 pts
# 4 - (-15) pts
# 5 - (-5) pts
# 6 - (-1) pts

# use random function to pick nums from 1 to 6
# pick numbers for each turns 
# add points according to the respective numbers choosen from random 

import random

dice = [1,2,3,4,5,6]


def points_marking(num):
    if num == 1:
        return 1
    elif num == 2:
        return 5
    elif num == 3:
        return 15
    elif num == 4:
        return -15
    elif num == 5:
        return -5
    else:
        return -1

def player_turns():
    play1_points = 0
    play2_points = 0
    count1 = 0
    count2 = 0
    while( play1_points < 100 and play2_points < 100 ):
        play1_turn = input("Player 1 turn \n PRESS ANY KEY TO CONTINUE : ")
        if play1_turn:
            random1 = random.choice(dice)
            play1_points += points_marking(random1)
            count1 += 1
        play2_turn = input("Player 2 turn \n PRESS ANY KEY TO CONTINUE : ")
        if play2_turn:
            random2 = random.choice(dice)
            play2_points += points_marking(random2)
            count2 += 1
             
    if play1_points>=100:
        print("PLayer 1 won the game !!! at ",count1," round")
        
    else:
        print("Player 2 won the game !!! at ",count2," round")

player_turns()      