#Holiday Checklist

print("---Holiday Checklist ---")

#Empty Arrays

packList = []
tasks = []

#Get user info

destination = str(input("Enter Name: "))
itemsNum = int(input("How many items do you wish to pack?: "))
tasksNum = int(input("How many tasks do you need to complete?: "))

#Loops

for i in range(0, itemsNum):
    packList.append(input("Enter item: " + str(i+1) + ": "))


for i in range(0, tasksNum):
    tasks.append(input("Enter Task: " + str(i+1) + ": "))


#Writing to a file

file = open(destination + "checklist.txt", "w")

for item in packList:
    file.write(item + "\n")

file.write("Tasks: \n")
for item in tasks:
    file.write(item + "\n")

file.close()
print("Your data has been saved")

