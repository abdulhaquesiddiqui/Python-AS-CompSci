print("Welcome to the number saving program!")
number = int(input("Please enter a whole number: ")

file = open("student.txt" , "a")
file.write(number)
file.close()
print("Details Saved")
