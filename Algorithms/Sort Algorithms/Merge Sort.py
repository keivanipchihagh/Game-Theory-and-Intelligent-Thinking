import random

def merge_sort(array):

    # Return condition
    if len(array) <= 1:
        return

    # Find middle
    middle = len(array) // 2

    # Find left hand
    left_side = array[:middle]

    # Find right hand
    right_side = array[middle:]

    # Sort first half
    merge_sort(left_side)

    # Sort second half
    merge_sort(right_side)

    i = j = k = 0

    # Rearrange array
    while i < len(left_side) and j < len(right_side):

        if left_side[i] < right_side[j]:
            array[k] = left_side[i]
            i += 1
        else:
            array[k] = right_side[j]
            j += 1
        
        k += 1

    # Add remaining elements
    while i < len(left_side):
        array[k] = left_side[i]
        i += 1
        k += 1

    while j < len(right_side):
        array[k] = right_side[j]
        j += 1
        k += 1

# Driver method
if __name__ == "__main__":
    array = random.sample(range(30), 10)

    print('Initial Array:', array)
    merge_sort(array = array)
    print('Sorted Array:', array)