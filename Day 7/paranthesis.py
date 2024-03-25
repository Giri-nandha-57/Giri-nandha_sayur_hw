# paranathesis using stack algorithm 
user_inp = list(input("Enter the string : ").split(" "))# getting multiple inputs and sep using " "
for i in user_inp:
    stack = []
    flag = 0
    for j in i:
        if j == "(":
            stack.append(j)# if j is equal to open bracket append it to stack list
        elif len(stack)==0 and j == ")":# if we have close bracket in starting of stack increment flag
            flag+=1
        elif j == ")":# perform pop when j is equal to close bracket 
            stack.pop()
    if len(stack) == 0 and flag == 0:# print i if it is valid input 
        print(i)
