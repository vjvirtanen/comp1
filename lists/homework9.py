def transpose(a):
    newlst = []

    for n in range(len(a[0])):
        row = []

        for i in range(len(a)):
            row.append(a[i][n])

        newlst.append(row)

    return newlst

print(transpose([[1, 2, 3], [4, 5, 6]]))

