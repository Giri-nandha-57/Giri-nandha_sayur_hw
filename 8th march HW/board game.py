# You have a 6 x 6 board. 
# Users take turns rolling the dice twice. first roll is row no, second roll is col number. Mark the spot (row, col) as claimed by the user
# who rolled the dice.
# When the user rolls the dice within 1 col/row of a claimed spot of the other user, the other user gets a point. 
# If the spot is same as the claimed spot of the other user, the user that rolled the dice gets a point. 
# The player who gets 5 points first wins the game. 

# create a board array of 6 rows and 6 columns 
# two users will roll the dice twice per turn 
# first roll is row and second roll is col
# mark the spot of row and col in the board array for the rolled user
# 
# if the spot is already claimed by other user then 1 point will be added to rolled user
# the player who gets 5 points first wins the game

import random

dice = [0,1,2,3,4,5]
board = []
ROW = int(input("Enter the no of rows : "))
COL = int(input("Enter the no of cols : "))  
A_points = [0]
B_points = [0] 

def play_spot_assign(row,col,player):
    if player == "A":
        if board[row][col]=="B":
            A_points[0]+=1
            board[row][col]="A"
            return
        board[row][col]="A"
        if row == 0 and (col != 5 and col != 0):
           if (board[row+1][col]=="B")or(board[row][col-1]=="B"or board[row][col+1]=="B"): 
               B_points[0]+=1
               return 
        if row == 5 and (col != 5 and col != 0):
           if (board[row-1][col]=="B")or(board[row][col-1]=="B"or board[row][col+1]=="B"): 
               B_points[0]+=1
               return
        if col == 0 and (row != 5 and row != 0) :
           if (board[row+1][col]=="B")or(board[row-1][col]=="B"or board[row][col+1]=="B"): 
               B_points[0]+=1
               return
        if col == 5 and (row != 5 and row != 0):
           if (board[row+1][col]=="B")or(board[row-1][col]=="B"or board[row][col-1]=="B"): 
               B_points[0]+=1
               return
        
        if row == 0 and col == 0:
           if (board[row+1][col]=="B"or board[row][col+1]=="B"): 
               B_points[0]+=1
               return
        if row == 5 and col == 5:
           if (board[row-1][col]=="B"or board[row][col-1]=="B"): 
               B_points[0]+=1
               return
        if row == 5 and col == 0:
           if (board[row-1][col]=="B"or board[row][col+1]=="B"): 
               B_points[0]+=1
               return
        if row == 0 and col == 5:
           if (board[row+1][col]=="B"or board[row][col-1]=="B"): 
               B_points[0]+=1
               return       
    
    if player == "B":
        if board[row][col]=="A":
            B_points[0]+=1
            board[row][col]="B"
            return
        board[row][col]="B"
        if row == 0 and (col != 5 and col != 0):
           if (board[row+1][col]=="A")or(board[row][col-1]=="A"or board[row][col+1]=="A"): 
               A_points[0]+=1
               return
        if row == 5 and (col != 5 and col != 0):
           if (board[row-1][col]=="A")or(board[row][col-1]=="A"or board[row][col+1]=="A"): 
               A_points[0]+=1
               return
        if col == 0 and (row != 5 and row != 0) :
           if (board[row+1][col]=="A")or(board[row-1][col]=="A"or board[row][col+1]=="A"): 
               A_points[0]+=1
               return
        if col == 5 and (row != 0 and row  != 5):
           if (board[row+1][col]=="A")or(board[row-1][col]=="A"or board[row][col-1]=="A"): 
               A_points[0]+=1
               return
               
        if row == 0 and col == 0:
           if (board[row+1][col]=="A"or board[row][col+1]=="A"): 
               A_points[0]+=1
               return
        if row == 5 and col == 5:
           if (board[row-1][col]=="A"or board[row][col-1]=="A"): 
               A_points[0]+=1
               return
        if row == 5 and col == 0:
           if (board[row-1][col]=="A"or board[row][col+1]=="A"): 
               A_points[0]+=1
               return
        if row == 0 and col == 5:
           if (board[row+1][col]=="A"or board[row][col-1]=="A"): 
               A_points[0]+=1
               return

def board_init():
    for i in range(ROW):
        board.append([])
        for j in range(COL):
            board[i].append(0)
            
def players_turn():
    while A_points[0]<5 and B_points[0]<5:
        play1_turn = input("Player 1 turn \n PRESS ANY KEY TO CONTINUE : ")
        if play1_turn:
            row1 = random.choice(dice)
            col1 = random.choice(dice)
            print(row1)
            print(col1)
            play_spot_assign(row1,col1,"A")
            for i in range(ROW):
                print(board[i])
                print()
            print("player 1 points = ",A_points[0])
            print("player 2 points = ",B_points[0])
        play2_turn = input("Player 2 turn \n PRESS ANY KEY TO CONTINUE : ")
        if play2_turn:
            row2 = random.choice(dice)
            col2 = random.choice(dice)
            print(row2)
            print(col2)
            play_spot_assign(row2,col2,"B")
            for i in range(ROW):
                print(board[i])
                print()
            print("player 1 points = ",A_points[0])
            print("player 2 points = ",B_points[0])
    if A_points[0] >= 5:
        print("Player 1 won the game !!! \n")
    elif B_points[0]>=5:
        print("Player 2 won the game !!! \n")        

board_init()
players_turn()