'''HW : Write program to simulate a ticketing system in an amusement park. 

Get input for a party with user’s name and birthday(date, month, year). 

Calculate price based on age (kids , senior cotizen : 50rs, adults : 75). 

On Tuesdays and Thursdays give 20% discount on total cost of tickets. 

Use relevant dateTime modules in python'''


import sys#imported needed modules
from datetime import time
from datetime import date
from datetime import datetime

def check_birthday_or_not(current_date,birth_date):#checkinng whether it is user birthday or not

    if(current_date.day==birth_date.day and current_date.month==birth_date.month):
        return True
    return False
def age(current_date,birth_date):#checking the user age by comparing his /her birthay with the current date
    if(current_date.month>birth_date.month):
            return current_date.year-birth_date.year
    elif(current_date.month==birth_date.month):
        if (current_date.day >= birth_date.day):
            return current_date.year - birth_date.year
    return current_date.year-birth_date.year-1
def entry_fees(age_of_uesr):#alloocating fees user according to his/her age
    if(age_of_uesr>=18 and age_of_uesr<=60):
        return 100
    return 50
collcection = 0
current_date=date.today()
print("\t\t\t SIT TICKET SERVICE")
person=int(input("1.Enter the no of user you need to take ticket"))
for i in range(person):
    print("person",person,"birthday date")
    birth=input("in the format of(dd/mm/yy)")
    birth_date=birth.split("/")
    for i in range(3):
        birth_date[i]=int(birth_date[i])
    if(birth_date[0]>=32 or birth_date[0]<=0 or birth_date[1]>=13 or birth_date[1]<=0 or birth_date[2]>  datetime.now().year):
        print("invalid birthday type")
        sys.exit(0)
    birth_date= date(birth_date[2],birth_date[1],birth_date[0])
    #print(birth_date.year)
    yes_or_no = check_birthday_or_not(current_date,birth_date)
    if(yes_or_no):
        print("its is free for person",i)
        continue
    age_of_user=age(current_date,birth_date)
    collcection = collcection +entry_fees(age_of_user)
if(current_date.weekday()==3 or current_date.weekday()==1):
    collcection = collcection - (collcection*0.2)
    print("after componsation your total bill is",collcection)
    sys.exit(0)
print(collcection)