a = int(input('a: '))
b = int(input('b: '))

if a >= 100:
    if b <= 50:
        print('1')
else:
    print('0')

if a >= 100:
    if b <= 50:
        print('1')
    else:
        print('0')
else: 
    if b >= 100:
        if a <= 50:
            print('1')
        else:
            print('0')
    else:
        print('0')
# useless comment
# another one