import random


def initialDetail():
    print("Welcoming to the Eisteddfod! Please answer the following")
    indoorOutdoor = int(input("Would you like: 1)Indoor stall 2)Outdoor stall "))
    if indoorOutdoor == 1:
        indoor()
    elif indoorOutdoor == 2:
        outdoor()



def indoor():
    storeReasonI = input("Please enter your reason for holding a store")
    fullNameI = input("Please enter your full name")
    emailI = input("Please enter your email address")
    daysBookingI = int(input("How many days will you be booking for?"))
    bookingNumberI = random.randint(1000,9999)
    totalCostI = 500*daysBookingI
    file = open(fullNameI+bookingNumberI+".txt", "w")
    file.write(fullNameI)
    file.write(emailI)
    file.write(storeReasonI)
    file.write(bookingNumberI)
    file.write(daysBookingI)
    file.write(totalCostI)
    file.close()
    print("Details Saved!")
    
    
def outdoor():    
    storeReasonO = input("Please enter your reason for holding a store")
    fullNameO = input("Please enter your full name")
    emailO = input("Please enter your email address")
    stallSize = int(input("How big do you want your stall? 1)Small 2)Medium 3)Large"))
    if stallSize == 1:
        cost = 125
        daysBookingO = int(input("How many days will you be booking for?"))
        bookingNumberO = random.randint(1000,9999)
        totalCostO = cost*daysBookingO
        print(totalCostO)
        file = open(fullNameO,bookingNumberO,".txt", "w")
        file.write(fullNameO)
        file.write(emailO)
        file.write(storeReasonO)
        file.write(bookingNumberO)
        file.write(daysBookingO)
        file.write(totalCostO)
        file.close()
        print("Details Saved!")
    elif stallSize == 2:
        cost = 150
        daysBookingO = int(input("How many days will you be booking for?"))
        bookingNumberO = random.randint(1000,9999)
        totalCostO = cost*daysBookingO
        print(totalCostO)
        file = open(fullName+bookingNumber+".txt", "w")
        file.write(fullNameO)
        file.write(emailO)
        file.write(storeReasonO)
        file.write(bookingNumberO)
        file.write(daysBookingO)
        file.write(totalCostO)
        file.close()
        print("Details Saved!")
    elif stallSize == 3:
        cost = 200
        daysBookingO = int(input("How many days will you be booking for?"))
        bookingNumberO = random.randint(1000,9999)
        totalCostO = cost*daysBookingO
        print(totalCostO)
        file = open(fullName+bookingNumber+".txt", "w")
        file.write(fullNameO)
        file.write(emailO)
        file.write(storeReasonO)
        file.write(bookingNumberO)
        file.write(daysBookingO)
        file.write(totalCostO)
        file.close()
        print("Details Saved!")
    else:
        print("Choose an existing option")
    

    
def retrieveDetails():
    print("Search for details to be retrieved")
    firstName = input("Please enter your first name")
    surname = input("Please enter your surname")
    try:
        file=open(firstName+surname+".txt", "r")
        firstName = file.readline()
        surname = file.readline()
        address = file.readline()
        dateOfBirth = file.readline()
        email = file.readline()
        print("Hello " + firstName + surname)
        print("DOB: " + dateOfBrith)
        print("Address: " + address)
        print("Email: " + email)
    except:
        print("No File Found")


print("Eisteddfod Booking Program")
option = input("""Please select from the following
1. New Booking
2. Retrieve Existing Booking""")


if option == "1":
    initialDetail()
elif option == "2":
    retrieveBOoking()
else:
    print("You need to choose an existing option")


