lst = []
i = 0

while i**2 < 50:
    lst.append(i**2)
    i += 1

print(lst) 

lst.clear()

lst = [i**2 for i in range(50) if i**2 < 50]

print(lst)