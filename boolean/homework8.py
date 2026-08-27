n = 2

while n <= 100:
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    if prime == True:
        print(n)
    n += 1



n = 2
primes = 0

while primes < 100:
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    if prime == True:
        print(n)
        primes += 1
    n += 1
