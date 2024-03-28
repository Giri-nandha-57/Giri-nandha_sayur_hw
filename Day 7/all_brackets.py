# paranathesis using stack algorithm 
user_inp = list(input("Enter the string : ").split(" "))# getting multiple inputs and sep using " "

def check_last_element(stack):
    return stack[-1]# return the last element is the stack list

for i in user_inp:
    stack = []
    for j in i:
        copy = ""
        if j == "(" or j == "{" or j == "[":
            stack.append(j)# if j is equal to any of the open bracket append it to stack list
        elif len(stack)==0 and (j == ")" or j == "}" or j == "]"):# if we have any of the close bracket in starting of stack increment flag
            break
        elif j == ")" or j == "}" or j == "]":
            if j == "]" and check_last_element(stack)== "[" :# check for the respective open bracket in stack
                stack.pop()
            if j == "}" and check_last_element(stack)== "{" :# check for the respective open bracket in stack
                stack.pop()
            if j == ")" and check_last_element(stack)== "(" :# check for the respective open bracket in stack
                stack.pop()
        copy = i
    if len(stack) == 0 and copy !="":# print i if it is valid input 
        print(i,"is a valid input ")
    else:
        print("not a valid input ")
