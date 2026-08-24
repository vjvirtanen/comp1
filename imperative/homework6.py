weight = int(input('Weight: '))

if weight <= 2:
    price = 3
elif weight <= 5:
    price = 3 +  2 * (weight - 2)
else:
    price = 6 + 3 * (weight - 5)

print(price)