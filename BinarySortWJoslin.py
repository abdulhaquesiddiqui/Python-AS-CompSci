#Binary Search
def binary_search(sorted_collection, target_value):
    lower_bound_index = 0
    upper_bound_index = len(sorted_collection) - 1

    while lower_bound_index <= upper_bound_index:
        middle_index = (lower_bound_index + upper_bound_index) // 2
        middle_value = sorted_collection[middle_index]

        if middle_value == target_value:
            return middle_index
        elif target_value < middle_index:
            upper_bound_index = middle_index - 1
        else:
            lower_bound_index = middle_index + 1

    return None

#Main Prog
my_Sorted_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

target = int(input("Enter search: "))

results = binary_search(my_Sorted_list, target)

if results is not None:
    print("Target found as Index")

else:
    print("Target not found")
    
