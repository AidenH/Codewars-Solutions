def Descending_Order(num):
    return int(''.join(sorted(list(str(num)), reverse=True)))


# Refactored from:
#
# def Descending_Order(num):
#     num_list = sorted(list(str(num)), reverse=True)
#     return int(''.join(num_list))
#
