n = int(input('n: '))
prime = True

for i in range(2, n):
    if n % i == 0:
        prime = False
        break

if n < 2:
    prime = False
    
print(prime)