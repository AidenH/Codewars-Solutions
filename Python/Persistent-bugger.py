from functools import reduce
def persistence(n):
    a = 0
    while len(list(str(n))) != 1:
        n = reduce(lambda x, y: x*y, [int(i) for i in str(n)])
        a += 1
    return a
