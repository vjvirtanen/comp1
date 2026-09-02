lst = []
while True:
    i = int(input('i: '))
    if i < 0:
        break
    if i not in lst:
        lst.insert(0, i) 
    else:
        lst.remove(i)
        lst.insert(0, i)

print(lst)