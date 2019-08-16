def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1
n = "XI"
i = 0
le = len(n)
res = 0
while (i < le):
    s1 = value(n[i])
    if (i + 1 < le):
        s2 = value(n[i + 1])
        if (s1 >= s2):
            res += s1
            i += 1
        else:
            res += s2 - s1
            i += 2
    else:
        res += s1
        i += 1
print(res)
