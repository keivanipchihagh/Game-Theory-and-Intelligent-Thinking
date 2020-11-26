# Import libraries
import random

# Simulation settings
length = 10
debug = False

# Make a list
arr = [i for i in range(length)]

# Shuffle the list
random.shuffle(arr)

for i in range(len(arr)):

    # Find the minimum index
    min_index = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap
    arr[i], arr[min_index] = arr[min_index], arr[i]

    # Print details
    if debug:
        print(arr)
    

# Print the sorted list
print(arr)

# Just to make sure
print('Sorted:', [i for i in range(len(arr))] == arr)
