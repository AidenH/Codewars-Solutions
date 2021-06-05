# Write a function, persistence, that takes in a positive parameter num and 
# returns its multiplicative persistence, which is the number of times you
# must multiply the digits in num until you reach a single digit.

from functools import reduce
def persistence(n):
    a = 0
    while len(list(str(n))) != 1:
        n = reduce(lambda x, y: x*y, [int(i) for i in str(n)])
        a += 1
    return a
