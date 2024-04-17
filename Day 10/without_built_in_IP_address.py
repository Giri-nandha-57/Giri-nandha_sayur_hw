"""problem 1"""
"""
    In an ip address there will be 3 "." 
    and 4 set of three/two digit numbers
    the numbers will be " 0 <= number <= 255 "
"""

user_ip_add = input("Enter the ip address : ")
list_ip_add = user_ip_add.split(".")

if len(list_ip_add) == 4:
    for i in list_ip_add:
        flag = 0
        if int(i) > 255 and int(i) < 0:
            print("Invalid ip ")
            flag = 1
            break
        else:
            continue
    print("Valid ip ")

else:
    print("Invalid ip ")
