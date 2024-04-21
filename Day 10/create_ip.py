# make an ip address from the given string of numbers
# if the numbers are enough to create an ip
# create a correct / valid
# the correct/valid constrain for an ip is
# ->  four numbers separated by "."
# the four numbers should be <256 and >0

# examples of ip are
# -> 1.1.1.1
# -> 12.2.12.4
# -> 233.0.9.203

user_input = list(input("Enter the string of numbers : "))  # getting the string input
length_of_input = len(user_input)  # storing the length of numbers

minimum_len = 4  # minimum length required to create an ip is 4
additional_digits = length_of_input - minimum_len + 1  # store the additional/extra digits
#                                                   ^ +1 is for considering the first number
ip = []
num = 0

if length_of_input < minimum_len:  # minimum numbers req to create an ip is 4
    print("length of the given date = ", length_of_input)
    print("The given data is not enough to create an ip address ")

else:
    for i in user_input:
        number = int(i)
        if additional_digits == 0:  # if there is no additional digits left then append number as it is to list
            ip.append(num)
            num = number  # store the current i/number to num variable
        else:
            duplicate = num * 10 + number
            if duplicate > 255:
                ip.append(num)
                num = number
            else:
                num = num * 10 + number
                additional_digits -= 1

    ip.append(num)  # append the last digit to list


#  To print
if len(ip) > 4:
    print("Provided input can't create an ip address !!!")
    print("The result would look like this = ", ip)
else:
    ip_string = ""
    sep_count = 3
    for i in ip:
        if sep_count>0:
            ip_string = ip_string + str(i) + "."
            sep_count -= 1
        else:
            ip_string = ip_string + str(i)
    print("valid ip can be = ", ip_string)
