def accum(s):
    a = []
    for i, item in enumerate(s, start=1):
        a.append(str(i * item).capitalize())
    return '-'.join(a)
