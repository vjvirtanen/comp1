result = ''
for i in range(10, 38, 3):
    result += str(i) + ', '
print(result[:-2])
print()

for i in range(998, 899, -2):
    print(i, end=' ')

print()

for i in range(1, 21):
    if i % 2 != 0:
        print(1, end=' ')
    else:
        print(-1, end=' ')