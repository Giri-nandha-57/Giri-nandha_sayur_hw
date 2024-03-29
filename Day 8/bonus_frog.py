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
