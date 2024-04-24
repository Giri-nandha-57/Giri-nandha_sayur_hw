from re import *

user_inp = input("Enter the sentence : ")

pattern = r'[0-9]+'

result = findall(pattern, user_inp)

print(result)
