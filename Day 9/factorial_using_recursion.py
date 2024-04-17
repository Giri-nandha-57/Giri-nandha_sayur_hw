# find the factorial for the given n number
# eg : fact(5) = 120
# pass n as argument and use recursion until we find the factorial value of the n number

fact_num = 1

def fact(num):
    global fact_num
    if num<=0:
        return fact_num
    return  num * fact(num-1)


user_inp = int(input("Enter the input to find factorial : "))
print(fact(user_inp))