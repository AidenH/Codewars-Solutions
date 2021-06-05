# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    a = []
    for i, item in enumerate(s, start=1):
        a.append(str(i * item).capitalize())
    return '-'.join(a)
