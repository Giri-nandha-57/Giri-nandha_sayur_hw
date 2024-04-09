onion_dict = {"Chennai": 30, "Trichy": 27, "Madurai": 34}
tomato_price = 10.5

def veggi_buggie(city, budget):
    global tomato_price
    petrol_expense = (budget * 0.03)
    budget -= petrol_expense

    onion_price = onion_dict[city]
    onion = int(budget // onion_price)
    tomato = int(budget // tomato_price)
    print(budget/tomato_price)
    print(f"Onion count : {onion} , Tomato count : {tomato}")


City = input("Enter the city : ")
Budget = int(input("Enter the budget : "))

veggi_buggie(City, Budget)
