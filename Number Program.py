print("Welcome to the number program!!!")

numberOfNumbers = int(input("How many numbers do you want to enter? "))

total = 0
mean = 0
maximum = 0
minimum = 9999999
numRange = 0


for i in range(0, numberOfNumbers):
    number = int(input("Enter a number: "))
    total = total + number
    mean = total/numberOfNumbers
    numRange =  maximum - minimum
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number

    numrange =  maximum - minimum

print("The total is: " + str(total))
print("The mean value: " + str(mean))
print("The minimum value is: " + str(minimum))
print("The maximum value is: " + str(maximum))
print("The range value is: " + str(numRange))


file = open("nameOfFile.txt", "w")
file.write(str(mean))
file.write(str(minimum))
file.write(str(maximum))
file.write(str(numRange))
file.close()


        
    
    
