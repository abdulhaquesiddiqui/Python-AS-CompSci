ISBN = input("Enter ISBN number: ")
checkDigit = ISBN[6]
total = 0
i = 0

for x in range(6):
    digit = (int(ISBN[i]) * 1)
    digit2 = (int(ISBN[i+1]) * 3)
    total = total digit + digit2
    i = i + 2

print(total)

check = total % 10
print(check)
remainder = 10 - check
print(remainder)


if remainder == checkDigit:
    print("Valid ISBN")
else:
    print("Invalid ISBN")
