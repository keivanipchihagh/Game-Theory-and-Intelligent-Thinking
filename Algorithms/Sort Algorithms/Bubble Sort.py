# Import libraries
import random

# Settings
length = 10
debug = False

# Create a list
arr = [i for i in range(length)]

# Shuffle the list
random.shuffle(arr)

# Algorithm
for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    if debug:
        print(arr)

print(arr)
print('Sorted: ', [i for i in range(length)] == arr)
