def enterDetails():

    print("Student Details Program: ")
    name = input("Please enter your name: ")

    age = input("Please enter your age")
    while age == "":
        print("You must enter your age: ")
        age = input("Please enter your age: ")

    email = input("Please enter your email: ")
    while not "@" in email:
        print("Email format invalid")
        email = input("PLease enter your email")

    file = open("student.txt" , "a")
    file.write(name)
    file.write("\n")
    file.write(age)
    file.write("\n")
    file.write(email)
    file.close()
    print("Details Saved")

    menu()

def checkage():
    checkName = input("Please enter your name: ")
    file = open("student.txt", "r")
    for line in file:
        if file.readline() == checkName:
            Found = True
        else:
            Found = False



        if Found == True:
            print("Found Name!")
        else:
            print("Name not found!")

    menu()

def menu():
    option = input("""What do you want to do?
a) Enter Details
b) View Details""")
    if option == "a":
        enterDetails()
    elif option == "b":
        checkage()
    else:
        print("No valid option chosen")

menu()
