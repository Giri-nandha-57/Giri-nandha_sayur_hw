# parking lot 
# create a 2d array 
# initialize array with 0 
# get carID from entering cars
# modify the values from 0 to carID
# change the values back to 0 when the car is leaving
# get toll fee from the leaving cars  
# count the number of vehicles parked in the lot 
# print the collected toll fee and parking lot when ever requested

parkinglot = []
toll_fee_collection = 0
rows = int(input("Enter the no of rows : "))
cols = int(input("Enter the no of cols : "))
parked_vehicles = 0

def init_parkinglot(rows,cols):
    for i in range(rows):
        parkinglot.append([])
        for j in range(cols):
            parkinglot[i].append(0)
            
def toll_info(toll_fee_collection):
    print("Toll collected so far : ",toll_fee_collection)
    withdraw = input("Would you like to withdraw the toll collection ..? y/n ")
    if withdraw == 'y':
        toll_fee_collection = 0
    return parking_management(parked_vehicles,toll_fee_collection)
            
def entering(carid,parked_vehicles):
    if parked_vehicles == rows*cols:
        print("SRY no more space left to park you vehicle ")
        return parking_management(parked_vehicles,toll_fee_collection)
    for i in range(len(parkinglot)):
        for j in range(len(parkinglot[i])):
            if parkinglot[i][j] == 0:
                parkinglot[i][j]=carid  
                parking_slot = str(i)+str(j)
                parked_vehicles += 1
                print("your car ",carid," is located at : ",parking_slot)
                return parking_management(parked_vehicles,toll_fee_collection)
            
def leaving_with_carID(carid,parked_vehicles,toll_fee_collection):
    for i in range(len(parkinglot)):
        for j in range(len(parkinglot[i])):
            if parkinglot[i][j] == carid:
                parkinglot[i][j]=0
                parked_vehicles -= 1
    toll_fee_collection += 50
    return parking_management(parked_vehicles,toll_fee_collection)
                
def parking_management(parked_vehicles,toll_fee_collection):
    print("Enter your choice from below options \n")
    choice = int(input("1. Park your vehicle \n2. Exit from parking \n3. Toll fee info \n4. show the parking lot \n5. END \nNOTE : Parking Toll Fee is 50 rs\n"))
    if choice == 1:
        carid = int(input("Enter your carID : "))
        entering(carid,parked_vehicles)
    elif choice == 2:
        card_ID_or_slot_ID = input("To leave by using car id press 'c'\nTo leave by using slot id press 's'\n")
        if card_ID_or_slot_ID == 'c':
            carid = int(input("Enter your car id : "))
            leaving_with_carID(carid,parked_vehicles,toll_fee_collection)
        elif card_ID_or_slot_ID == 's':
            slot_id_row = int(input("Enter the first digit in slot id : "))
            slot_id_col = int(input("Enter the second digit in slot id : "))
            parkinglot[slot_id_row][slot_id_col] = 0
            parked_vehicles -= 1
            toll_fee_collection += 50
            return parking_management(parked_vehicles,toll_fee_collection)
    elif choice == 3:
        access_code = input("Enter the access code to access 'private use only'\n")
        if access_code == "GiriToll24":
            toll_info(toll_fee_collection)
        else:
            print("Access Denied ")
            return parking_management(parked_vehicles,toll_fee_collection)
    elif choice == 4:
        print(parkinglot)
        return parking_management(parked_vehicles,toll_fee_collection)
    elif choice == 5:
        return 0    
init_parkinglot(rows,cols)
parking_management(parked_vehicles,toll_fee_collection)