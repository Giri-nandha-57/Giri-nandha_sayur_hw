inp = [4,5,6,5,3,2,1]
stack = [0]
for i in inp:
    index = len(stack)-1
    if stack[index]<i:
        i += stack[index]
        stack.pop()
        stack.append(i)
    else:
        stack.append(i)
print(stack)
