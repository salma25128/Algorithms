
#-insertion_sort>>> cards arrangement algo
# ******************************************
# Initialization: Start with the second element of the array (index 1) as the key, and compare it to the elements before it
# Comparison: Compare the key with each element to its left, shifting elements that are greater than the key to the right.
# Insertion: Once the correct position is found, insert the key at that position.
# Repeat: Move to the next element and repeat until the entire array is sorted.

def insertion_sort(input_list):
    for index in range(1, len(input_list)):
        current_value = input_list[index]
        position = index

        while position > 0 and input_list[position - 1] > current_value:
            input_list[position] = input_list[position - 1]
            position -= 1

        input_list[position] = current_value

    return input_list


print(insertion_sort([25,12,4,58,7,3,1]))


# ------------------------------------------------
def insertion_sort(arr):
    n = len(arr)
    print(f"n={n}")
    if n<=1:
        return
    for i in range(1,n):
        key = arr[i]
        j = i-1
        print(f"i={i} key={key} j={j}")         # always trace

        while j >= 0 and key < arr[j]:
            arr[j+1]=arr[j]
            # print(f"key*={key}and j*={j}")
            j-= 1
            arr[j+1]=key
            print(f"l-key={key}and j={j}")

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(f"result={arr}")




# //////////////////////////////////////////////////////////////////
# Algorithm Corectness:
# Loop Invariant Proof for Insertion Sort
# *********************************
# >> Invariant: At the start of each iteration of the outer loop (indexed by i), the subarray arr[0:i] is sorted.

# 1- Initialization: Before the first iteration (i = 1), the subarray arr[0:1] consists of just one element, arr[0], which is trivially sorted. So the invariant holds.

# 2 -Maintenance: During each iteration, the algorithm takes the key (which is arr[i]) and compares it with elements in the already sorted subarray arr[0:i].
#    It shifts all larger elements one position to the right until it finds the correct position for key.
#    After inserting key, the subarray arr[0:i+1] is sorted. Thus, the invariant is maintained.

# 3-Termination: The loop terminates when i reaches len(arr). At this point, the invariant ensures that arr[0:len(arr)] is sorted,
#    which means the entire array is sorted.