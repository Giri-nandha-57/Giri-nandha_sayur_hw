# Parking fee is 
# If you return within 15 mins, its free
# Rs 100 for the first hr
# Rs 150 for each hr after that. 
# Fee is calculated in 30 min increments. (meaning, if you spent 25 mins, you will be charged for 30 mins
# If you spend 35 mins, you will be charged for one hr)
# Get entry time and exit time from customer as input and display the fee.

parking_fee = [0]

def mins_calculator(time):
    hours = int(time[0])
    mins = int(time[1])
    mins = (hours*60) + mins
    
    return mins

def calculate_fee(Time):
    if Time == 1:
        parking_fee[0]+=50
        return
    else:
        parking_fee[0]+=100
        Time-=2
        while(Time>0):
            parking_fee[0]+=75
            Time-=1
        return 
        

def get_input():
    parked_time = list(input("Enter the time you parked  your vehicle in the given format \n 24 hrs time frame 00:00 \n ").split(":"))
    leaving_time = list(input("Enter the time you are leaving form parking in the given format \n 24 hrs time frame 00:00 \n ").split(":"))
    pt_mins = mins_calculator(parked_time)
    lt_mins = mins_calculator(leaving_time)
    parked_time_mins = lt_mins-pt_mins
    if parked_time_mins<=15:
        print("There is no fee for your parking !!\n")
        return 
    parked_time_half_hrs = -(parked_time_mins//-30)
    calculate_fee(parked_time_half_hrs)
    print("Total parking fee is  : ",parking_fee[0])
get_input()