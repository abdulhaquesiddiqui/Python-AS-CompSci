def menu():
    choice = input("""Please choose one of the following checks:
1. Verification
2. Validation - Length Check
3. Validation - Prescence Check
4. Validation - Range Check """)
    if choice == "1":
        dblEntry()
    elif choice == "2":
        lengthChk()
    elif choice == "3":
        presChk()
    elif choice == "4":
        rangeChk()
    else: print("Invalid Option Chosen")
    menu()


def dblEntry():
    wordEntered = input("Please enter a word: ")
    wordReEnter = input("Please enter the same word again: ")
    if wordEntered == wordReEnter:
        print("Success")
    else:
        print("You've not entered the same word")
        menu()
        
def lengthChk():
    phoneNum = input("Please enter your phone number: ")
    while len(phoneNum) != 11:
        print("Not 11 digits, try again!")
        phoneNum = input("Please enter your phone number: ")
        print("Phone number success")
        menu()
        

def presChk():
    name = input("Please enter your name: ")
    while name == "":
        print("You have not entered anything! ")
        name = input("Please try again, enter your name: ")
    print("Name Success")
    menu()


def rangeChk():
    age = int(input("Please enter your age: "))
    while age < 1 or age > 125:
        print("Age is out of range")



menu()
