#Bubble sort
username = ["Zain", "Carl", "Eric", "Zoe", "Alan", "Seth"]
numItems = 6
print("Unsorted List")
print(username)

while numItems > 1:
    for count in range(5):
        if username[count] > username[count + 1]:
            temp = username[count]
            username[count] = username[count + 1]
            username[count + 1] = temp
    numItems = numItems - 1

print("Sorted List")
print(username)
