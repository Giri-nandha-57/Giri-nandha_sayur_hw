from re import *

user_inp = input("Enter the sentence : ")

pattern = r'[a-zA-Z0-9]+'

result = findall(pattern, user_inp)

print(result)
