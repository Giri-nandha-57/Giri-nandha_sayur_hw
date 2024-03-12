User_input = str(input("enter string : "))
user_inp_words = User_input.split(" ")
empty= ""
for j in user_inp_words:
    if j not in empty:
        empty+=j + " "
        
print(empty)