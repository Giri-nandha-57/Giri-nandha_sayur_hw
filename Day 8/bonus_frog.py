inp = list(input("Enter the input : ").split(","))
stack = [0]
for i in inp:
    integ = int(i)
    index = len(stack)-1
    if stack[index]<integ:
        integ += stack[index]
        stack.pop()
        stack.append(integ)
    else:
        stack.append(integ)
print(stack)
