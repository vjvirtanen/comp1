while sun := input('sun shining (yes/no): '):
    if sun == 'yes' or sun == 'no':
        break

while time := int(input('time: ')):
    if time in range(24):
        break

if 10 <= time <= 16:
    print('Please use sunscreen.')