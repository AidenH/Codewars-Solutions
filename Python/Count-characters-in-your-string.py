from collections import Counter
def count(string): return Counter(list(string))


# Refactored from:
#
# def count(string):
#     a = {}
#     for i in list(string):
#         if i in a:
#             a[i] += 1
#         else:
#             a[i] = 1
#     return a
#
