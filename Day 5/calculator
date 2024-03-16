'''
user input can be a string to perform mathimatcal operations 

eg : 22+33/43-43-56+34*56
'''
import sys

str = []

def add(add_num,num):
    return add_num + num

def sub(sub_num,num):
    return sub_num - num

def mul(mul_num,num):
    return mul_num * num

def div(a,b):
    return a/b

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

def precedence(ip_str):
    for i in range(len(ip_str)):
        if ip_str[i] == '/':
            ip_str = division_oper(ip_str,i)
    for i in range(len(ip_str)):
        if ip_str[i] == '*':
            ip_str = multiplication_oper(ip_str,i)
    for i in range(len(ip_str)):    
        if ip_str[i] == '-':    
            ip_str = subraction_oper(ip_str,i)
    for i in range(len(ip_str)):    
        if ip_str[i] == '+':
            ip_str = addition_oper(ip_str,i)
    if len(ip_str) == 1:
        main(ip_str)

def user_input():
    str = list(input("Enter your input numbers with mathematical expressions eg  xx ( '+' or '-' or '*' or '/' ) yy : \n").split(" "))
    print(str)
    precedence(str)

def main(output_list):
    print("Output of the given expression is : ",output_list[0]) 
    sys.exit(0)

user_input()