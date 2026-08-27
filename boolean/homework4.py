a = int(input('a: '))
b = int(input('b: '))
i = 1

while i % a != 0 or i % b != 0:
    i += 1 

print(i)