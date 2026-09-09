lst = []
while True:
    i = int(input('i: '))
    if i < 0:
        break
    if i in lst:
        lst.remove(i)
    lst.insert(0, i)

print(lst)