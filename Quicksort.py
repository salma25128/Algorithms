
# divide & conquer algo

def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        smaller_num = [n for n in arr[1:] if n < pivot]
        larger_num = [n for n in arr[1:] if n > pivot]
    return quick_sort(smaller_num) + [pivot] + quick_sort(larger_num)

print (quick_sort([5, 10, 2, 3,25 ,12]))


# quicksort speed id depending on pivot choosen
# In the worst case:
# quicksort takes O(n 2) time. depending on pivot choosen


