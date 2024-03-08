User_input = str(input("enter string : "))
user_inp_words = User_input.split(" ")
empty= ""
for j in user_inp_words:
    upp = j.upper()
    low = j.lower()
    if upp not in empty and low not in empty:
        empty+=j + " "
        
print(empty)