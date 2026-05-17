import random #Library
print("Quiz")
firstname = str(input("Enter your name: "))
surname = str(input("Enter your surname: "))
password = random.randint(0000, 9999)
username = firstname[0] + surname[0:4]
print("Username is: " +  username)
print("Password is: ", password)

entUsername = str(input("Enter Username: "))
entPassword = int(input("Enter Password: "))
                  
while entUsername != username:
                  print("Incorrect details!!!")
                  entUsername = str(input("Enter Username: "))

while entPassword != password:
                  print("Incorrect details!!!")
                  entPassword = int(input("Enter Password: "))

print("Welcome " + username)
print("Make your selection")
score=0
choice = int(input(" 1) Easy \n 2) Medium \n 3) Hard \n"))
if choice == 1:
    print("Easy")
    q1 = str(input(" 1) What is the capital of Cardiff? ")
    q1.lower()
    if q1 == "cardiff":
             print("Correct Answer!")
             score = score + 1
             print("Score is " , score)
    else:
             print("Incorrect Answer")
             print("Score is ", score)



    print("Who held an event this week to launch a their techniology?")
    q2 = int(input("

    elif choice == 2:
        print("Medium")


    elif choice == 3:
        print("Hard")
