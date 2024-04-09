sentence = input("Enter the sentence ").split(" ")
stack = []
reverse_words = ""
for i in sentence:
    stack.append(i)

for i in range(len(stack)):
    reverse_words = reverse_words + stack.pop() + " "

print(reverse_words)
