# paranathesis using stack algorithm 
user_inp = list(input("Enter the string : ").split(" "))# getting multiple inputs and sep using " "
for i in user_inp:
    stack = []
    for j in i:
        copy = ""
        if j == "(":
            stack.append(j)# if j is equal to open bracket append it to stack list
        elif len(stack)==0 and j == ")":# if we have close bracket in starting of stack increment flag
            break
        elif j == ")":# perform pop when j is equal to close bracket 
            stack.pop()
        copy = i
    if len(stack) == 0 and copy !="":# print i if it is valid input 
        print(i)
    else:
        print("not a valid input ")
