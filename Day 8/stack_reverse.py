"""
Reverse a string: Given a string, reverse it using a stack.
Eg : Hello -> olleH
"""
inp = input("Enter a string : ")
stack = []
for i in inp:
    stack.append(i)
for i in range(len(inp)):
    print(stack.pop(),end="")
