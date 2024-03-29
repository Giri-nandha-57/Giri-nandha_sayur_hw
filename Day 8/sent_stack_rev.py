"""
Given string str, we need to print the reverse of individual words. (dont use built in functions)
Input : Hello World
Output : olleH dlroW
"""
sentence = input("Enter the sentence : ").split(" ")
for i in sentence:
    stack = []
    for j in i:
        stack.append(j)
    for j in range(len(i)):
        print(stack.pop(),end="")
    print(end=" ")
