# Your task is to make a function that can take any non-negative integer as an 
# argument and return it with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.

def Descending_Order(num):
    return int(''.join(sorted(list(str(num)), reverse=True)))


# Refactored from:
#
# def Descending_Order(num):
#     num_list = sorted(list(str(num)), reverse=True)
#     return int(''.join(num_list))
#
