import sys

string_in = []

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1//num2

def addition_oper(lst,i):
    index = i-1
    remain_num = (add(int(lst[i-1]),int(lst[i+1])))
    lst = lst[:i-1] + lst[i+2:]
    lst.insert(index,remain_num)
    print("after addition : ",lst)
    precedence(lst)

def subraction_oper(lst,i):
    index = i-1
    remain_num = (sub(int(lst[i-1]),int(lst[i+1])))
    lst = lst[:i-1] + lst[i+2:]
    lst.insert(index,remain_num)
    print("after subraction : ",lst)
    precedence(lst)

def multiplication_oper(lst,i):
    index = i-1
    remain_num = (mul(int(lst[i-1]),int(lst[i+1])))
    lst = lst[:i-1] + lst[i+2:]
    lst.insert(index,remain_num)
    print("after multiplication : ",lst)
    precedence(lst)

def division_oper(lst,i):
    index = i-1
    remain_num = (div(int(lst[i-1]),int(lst[i+1])))
    lst = lst[:i-1] + lst[i+2:]
    lst.insert(index,remain_num)
    print("after division : ",lst)
    precedence(lst)

def precedence(list_input):
    for i in range(len(list_input)):
        if list_input[i] == '/':
            list_input = division_oper(list_input,i)
    for i in range(len(list_input)):
        if list_input[i] == '*':
            list_input = multiplication_oper(list_input,i)
    for i in range(len(list_input)):    
        if list_input[i] == '-':    
            list_input = subraction_oper(list_input,i)
    for i in range(len(list_input)):    
        if list_input[i] == '+':
            list_input = addition_oper(list_input,i)
    if len(list_input) == 1:
        main(list_input)

def user_input():
    string_inp = list(input("Enter your input numbers with mathematical expressions eg  xx ( '+' or '-' or '*' or '/' ) yy : \n").split(" "))
    precedence(string_inp)

def main(output_list):
    print("Output of the given expression is : ",output_list[0]) 
    sys.exit(0)
    
user_input()

'''
eg : 
 
input = 22 / 34 * 34 / 24 + 20 - 39

output = -19

'''