# Finding the greatest common divisor(GCD) OF 2 Integers
# the largest no dividing both no without leaving a remainder
# GCD Property: If you have two numbers a and b, and a > b, then the GCD of a and b is the same as the GCD of b and a % b (where % is the modulus operator).
# Reduction Step: This means that instead of finding the GCD of a and b, you can reduce the problem to finding the GCD of b and a % b. This reduction process continues until the remainder becomes zero.
# Base Case: When the remainder (b in our case) becomes zero, the other number (a at that point) is the GCD.


# Recursive , divide&conquer and Greedy algorithm


def euclids(a,b):
    if b==0:
        return a
    else:
        return euclids(b,a % b )


print(euclids(200,50))
