def symm_diff(a, b):
    symm = []
    for n in a:
        if n not in b:
            symm.append(n)
    for m in b:
        if m not in a:
            symm.append(m)
    return symm

a = [4, 4, 6, 11, -2, 3]
b = [5, 11, 11, -3, 3, 5]

print(symm_diff(a, b))