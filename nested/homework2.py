a = [1, 2, 4]
b = [3, 5, 6, 2]
flag = False
for n in range(len(a)):
    for m in range(len(b)):
        if a[n] == b[m]:
            flag = True
            break

print(flag)