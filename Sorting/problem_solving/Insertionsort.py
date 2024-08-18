# Insertion Sort - Part 1
# https://www.hackerrank.com/challenges/insertionsort1/problem?isFullScreen=true

def insertionSort1(n, arr):
    key = arr[-1]
    i = n- 1
    while i > 0 and arr[i - 1] > key:
        arr[i] = arr[i - 1]
        print(*arr)
        i -= 1
    arr[i] = key
    print(*arr)
    return arr
print(insertionSort1(n=5,arr=[1,2,4,5,3]))


# Excecution:
# *******************************


# First Iteration of the While Loop:
# -----------------------------------
# The condition i > 0 and arr[i - 1] > key is checked:
# i = 4, so i > 0 is True.
# arr[i - 1] = arr[3] = 5, which is greater than key = 3.
# Shift Operation:
# arr[i] = arr[i - 1] shifts the value at arr[3] to arr[4].
# Array becomes: [1, 2, 4, 5, 5]
# Print: 1 2 4 5 5
# >>>>Update i:
#>>> Decrement i by 1, so now i = 3.
# Current State:
# ---------------
# key = 3
# i = 3
# Array: [1, 2, 4, 5, 5]

# Second Iteration of the While Loop:
# ----------------------------------
# The condition i > 0 and arr[i - 1] > key is checked again:
# i = 3, so i > 0 is True.
# arr[i - 1] = arr[2] = 4, which is greater than key = 3.
# Shift Operation:
# arr[i] = arr[i - 1] shifts the value at arr[2] to arr[3].
# Array becomes: [1, 2, 4, 4, 5]
# Print: 1 2 4 4 5
# Update i:
# Decrement i by 1, so now i = 2.
# Current State:
# key = 3
# i = 2
# Array: [1, 2, 4, 4, 5]


# Third Iteration (Exiting the Loop):
#-------------------------------------
# The condition i > 0 and arr[i - 1] > key is checked:
# i = 2, so i > 0 is True.
# arr[i - 1] = arr[1] = 2, which is not greater than key = 3.
# Since the condition arr[i - 1] > key is False, the loop exits.
# Insert the Key Element:
#
# After the loop exits, arr[i] = key places the key value 3 at index 2.

# Final State:
# -------------------
# Array: [1, 2, 3, 4, 5]
# ////////////////////////////////////////////////////////////////////////////////////////////////


# Insertion Sort - Part 2
# https://www.hackerrank.com/challenges/insertionsort2/problem?isFullScreen=true
def insertionSort2(n, arr):
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # print(*arr)

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]

            j -= 1
        arr[j + 1] = key
        print(*arr)
