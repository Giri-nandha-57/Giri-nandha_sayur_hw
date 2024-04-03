"""
There are frogs walking in a line represented in the form of a list. The numbers in the list are the size of frogs. A frog(at position i) will eat the previous frog (i-1), if the previous frog is smaller in size. Print the alive frogs in the list 

Input : [1,2,5,4,3,2,2]
Output : [5,4,3,2,2]
Explanation : Frog (1) ate Frog(0); Frog(2) ate Frog (1). Rest of the frogs are alive
Input : [4,3,3,2,1]
Output : [4,3,3,2,1]

same as above
add this constrain --> Imagine the frog becomes bigger as much as the size of the frog it ate. How would it change the program?

"""


def check(prev,integer_val):
    integer_val += stack[prev]
    stack.pop()
    return integer_val


inp = list(input("Enter the input : ").split(","))
stack = []
for i in inp:
    integer_of_i = int(i)
    while 1:
        index = len(stack)
        if index == 0:
            stack.append(integer_of_i)
            break
        elif stack[index-1] < integer_of_i:
            integer_of_i = check(index-1 , integer_of_i)
        else:
            stack.append(integer_of_i)
            break
print(stack)
