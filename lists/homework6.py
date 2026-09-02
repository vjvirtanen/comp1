import random
n = 10
flist = []
list_of_lists = [random.sample(list(range(n)), n) for _ in range(5)]
for l in list_of_lists:
    for x in l:
        flist.append(x)

print(flist)