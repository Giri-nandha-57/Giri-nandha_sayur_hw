User_input = str(input("enter string : "))
user_inp_words = User_input.split(" ")
empty_str = ""
for j in user_inp_words:
    empty = ""
    for i in j :
        upp = i.upper()
        low = i.lower()
        print(upp, low)
        if upp not in empty and low not in empty:
            empty+=i
    empty_str += empty + " "
print(empty_str)