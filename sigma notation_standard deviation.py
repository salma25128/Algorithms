# import math
#
# sd = ave = n = b = 0
# x = []
#
# n = int(input("n=? "))
#
# for i in range(n):
#     x.append(float(input(f"x[{i}] ")))
#     ave += x[i]
#
# ave /= n
#
# print(ave)


n = int(input("n = ? "))
x = []

for i in range(n):
    x.append(float(input("x[" + str(i) + "] = ")))

ave = sum(x) / n

print(ave)
