import random
r2 = 0

for i in range(10000):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        r2 += 1

print(r2 / 10000)