User_input = str(input("enter string : "))
user_inp_words = User_input.split(" ")
empty_str = ""
for j in user_inp_words:
    empty = ""
    for i in j :
        if i not in empty:
            empty+=i
    empty_str += empty + " "
print(empty_str)