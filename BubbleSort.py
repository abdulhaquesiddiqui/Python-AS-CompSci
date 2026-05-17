#usernames = ["Carl", "Alex", "Eric", "Dan", "Alan", "Mark"]
#numItems = 6
#print("Unsorted List")
#print(usernames) 

#while numItems > 1:
    #for count in range(5):
        #if usernames[count] > usernames[count + 1]:
            #temp = usernames[count]
            #usernames[count] = usernames[count + 1]
            #usernames[count + 1] = temp
    #numItems = numItems - 1


#print("Sorted List")
#print(usernames)


#Challenges
#Allow the ser to enter their own data into the array
#Ask the user how many pieces of data in the array


username = []
numItems = int(input("How many names would you like to enter: "))
for i in range(0, numItems):
    username.append(input("Enter name: " + str(i+1) + "; ")

print("Unsorted List")
print(username) 

while numItems > 1:
    for count in range(0, numItems):
        if username[count] > username[count + 1]:
            temp = username[count]
            username[count] = username[count + 1]
            username[count + 1] = temp
    numItems = numItems - 1


print("Sorted List")
print(username )
