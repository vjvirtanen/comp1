def share(a, b):
    for i in a:
        for j in b:
            if i == j:
                return True
    return False

print(share([1,2,3], [3,4,5]))