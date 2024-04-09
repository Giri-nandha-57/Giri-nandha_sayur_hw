
def assign_values(num, chrs, spc, length):
    if chrs >= 3 and num >= 2 and spc >= 1 and length >= 8:
        if length >= 16:
            return "Very strong"
        else:
            return "Strong"
    elif chrs >= 1 and num >= 1 and spc >= 1 and length >= 8:
        return "Ok"
    elif chrs >= 8 or num >= 8 or spc >= 8 and length >= 8:
        return "Weak"

def check_password(word, length):

    chars_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chars_high = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    char = 0
    number = 0
    special = 0

    for i in word:
        if i in numbers:
            number += 1
        elif i in chars_low or i in chars_high:
            char += 1
        else:
            special += 1
    return assign_values(number, char, special, length)


password = input("Enter the password : ")
print(check_password(password, len(password)))
