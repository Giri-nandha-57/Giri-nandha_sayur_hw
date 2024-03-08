User_input = str(input("enter string : "))
empty = ""
for i in User_input:
    if i not in empty:
        empty+=i
print(empty)