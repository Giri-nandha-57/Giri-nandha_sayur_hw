# Goal is to extract all the URL in the given sentence
#  example of URL :
#  ->  https://xxx.yyyy.zzz

from re import *

user_inp = input("Enter the sentence : ")

pattern = r'http[s]?://[a-zA-Z.]*[a-zA-Z]+'

result = findall(pattern, user_inp)

print(result)
