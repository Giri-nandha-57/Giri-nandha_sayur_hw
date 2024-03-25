user_inp = list(input("Enter the string : ").split(" "))
for i in user_inp:
    stack = []
    count = 0
    for j in i:
        if j == "(":
            stack.append(j)
        elif len(stack)==0 and j == ")":
            count+=1
        elif j == ")":
            stack.pop()
    if len(stack) == 0 and count == 0:
        print(i)
