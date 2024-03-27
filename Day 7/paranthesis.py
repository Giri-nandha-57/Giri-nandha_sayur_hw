# paranathesis using stack algorithm 
user_inp = list(input("Enter the string : ").split(" "))# getting multiple inputs and sep using " "
for i in user_inp:
    stack = []
    copy = ""
    for j in i:
        if j == "(":
            stack.append(j)# if j is equal to open bracket append it to stack list
        elif len(stack)==0 and j == ")":# if we have close bracket in starting of stack increment flag
            break
        elif j == ")":# perform pop when j is equal to close bracket 
            stack.pop()
        copy = i
    if copy != "":# print copy if it is valid input 
        print(copy)
    else:
        print("No valid input is given ")
