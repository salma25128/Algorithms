
# divide & conquer recursion technique
# break it to the smaller segments you will reach to the simplest form stop there it is>>>> a basecase

# sum list elements
# loops
def divide(arr):
    add = 0
    for i in arr:
        add += i
        print(f"show me what is happening: {add}")
    print(f"result is = {add}")
    return add

divide([1,2,3,5])
# ----------------------------------------------------------

# recursion
def divide_sum(arr):
    print(f"behind the seen : {arr}")
    if len(arr) == 1:        #basecase
        return arr[0]
    else:
      return (arr[0] + divide_sum(arr[1:]))    #recursivecase

print(divide_sum(arr=[1,2,3,5]))

