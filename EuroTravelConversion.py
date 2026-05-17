#EuroTravelConversion

menu = int(input("1) Pounds to Euros \n 2) Euros Pounds \n: 3) Pounds to Special Drawing Rights \n 4) Special Drawing Rights to Pounds \n: "))


if menu == 1:
    amount = float(input("Enter Pounds: "))

    if amount == float(amount):
        for i in range(-5, 5):
            euro = (amount + i) * 1.14
            euroR = round(euro, 2)
            print("£", amount + i, " = €", euroR)

    else:
        print("Please use correct numebr type")



if menu == 3:
    amount = float(input("Enter Pounds: "))

    if amount == float(amount):
        for i in range(-5, 5):
            specialDrawingRights = (amount + i) * 0.93
            SDRR = round(specialDrawingRights, 2)
            print("£", amount + i, " = ", SDRR)
 
    else:
        print("Please use correct numebr type")

elif menu == 4:
    print("Test")
