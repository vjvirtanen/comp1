numbers = []
numbers_once = []
while (i := int(input("i: "))) >= 0:
    numbers.append(i)
    if i not in numbers_once:
        numbers_once.append(i)

print(numbers_once)