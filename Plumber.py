print("Plumbers Program")

plumberName = input("Please enter a name: ")
while plumberName == "":
    print("Validation Failed - You must enter your name!")
    plumberName = input("Please enter a name: ")

plumberNumber = input("Please enter a phone number: ")
while len(plumberNumber) != 11:
    print("You must enter an 11 digit phone number!")
    plumberNumber = input("Please enter a phone number ")

plumberRate = float(input("Please enter your hourly rate: "))
while plumberRate < 0.99 or plumberRate > 15.01:
    print("Please enter a valid time rate!")
    plumberRate = input("Please enter your hourly rate: ")

plumberEmail = input("Please enter your email address: ")
while not "@" in plumberEmail:
    print("Please enter a valid email address! ")
    plumberEmail = input("Please enter your email address: ")


file = open("plumbers.txt", "a")
file.write(plumberName)
file.write(plumberNumber)
file.write(str(plumberRate))
file.write(plumberEmail)
file.write("\n")
file.close()

print("Details Saved")


