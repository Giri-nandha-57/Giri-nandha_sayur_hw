sentence = input("Enter the sentence : ").split(" ")
for i in sentence:
    stack = []
    for j in i:
        stack.append(j)
    for j in range(len(i)):
        print(stack.pop(),end="")
    print(end=" ")
