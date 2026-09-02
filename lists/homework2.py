negatives = []
positives = []

while True:
    i = int(input('i: '))
    if i == 0:
        break
    elif i < 0:
        negatives.append(i)
    else:
        positives.append(i)

print(positives)
print(negatives)