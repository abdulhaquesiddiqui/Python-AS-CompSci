num1 = int(input("Pick a number:"))
num2 = int(input("Pick a second number: "))


operator = int(input("Now pick an operator 1)Add 2)Subtract 3)Multiply 4)Divide"))

num3 = 0

if operator == "1":
    num3 = num1 + num2 + num3
    print("Your new number is: " , num3)

elif operator == "2":
    num3 = num1 - num2 + num3
    print("Your new number is: " , num3)

elif operator == "3":
    num3 = num1 * num2 + num3
    print("Your new number is: " , num3)

elif operator == "2":
    num3 = num1 / num2 + num3
    print("Your new number is: " , num3)
