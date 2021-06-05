# Count all the occurring characters in a string. If you have a string like aba,
# then the result should be {'a': 2, 'b': 1}.
#
# What if the string is empty? Then the result should be empty object literal, {}.

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
