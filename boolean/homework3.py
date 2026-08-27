s = int(input('s: '))
n = 1

while n**3 - 10*n**2 <= s:
    n += 1

print(n)