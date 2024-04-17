"""
    same constrains as prev problem
    -> but use regex library

"""
import re

user_inp_ip = input("Enter the ip address : ")
ip_list = user_inp_ip.split(".")
pattern = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{1,2}|[0-9]{1,2})$"
flag = 0
if len(ip_list) == 4:
    for i in ip_list:
        flag = 0
        if re.search(pattern, i):
            continue
        else:
            flag = 1
            break
else:
    print("Invalid ip ")
if flag == 0:
    print("Valid ip ")
else:
    print("Invalid ip ")
