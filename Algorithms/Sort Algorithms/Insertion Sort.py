# Import libraries
import random

# Simulation settings
debug = False
length = 10

# Make a list 0 - 10
arr = [i for i in range(length)]

# Shuffle the list
random.shuffle(arr)

# Insertion algorithm
for i in range(len(arr)):
    j = i

    # If the selected node is smaller than the previous one, shift left
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1

    # Print stuff out
    if debug:
        print(arr)    

# Print the result
print(arr)

# Just making sure
print('sorted: ', [i for i in range(len(arr))] == arr)
