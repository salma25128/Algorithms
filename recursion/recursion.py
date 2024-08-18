# simply recursion >>> when a function calls itself
# basecase >>> when should fn stop recursing? //

# recursivecase  >>>> when fn calls itself??

# ------------------------------------------------------------------|
#>>>“Loops may achieve a performance gain for your program.         |
# >>>Recursion may achieve a performance gain for your( programmer).|
#Choose which is more important in your situation!                  |
# ------------------------------------------------------------------|


def recursion(i):
    print(f"num: {i}")
    if i<=1:                              #basecase >>> exit condition
       return
    else:
     recursion(i-1)                             #recursivecase

recursion(8)
# ------------------------------------------------------------------------------------------------
# if we have no basecase
# ....>> infinite loop..>>>
# "RecursionError: maximum recursion depth exceeded while calling a Python object"
# stackoverflow
# def recursion(i):
#     recursion(i - 1)


