while True:
    s = input('my-calc: ')
    if s == '':
        break

    a, operator, b = s.split()
    a = int(a)
    b = int(b)

    if operator == '+':
        print(a + b)
    elif operator == '-':
        print(a - b)
    elif operator == '*':
        print(a * b)
    elif operator == '/':
        print(a / b)
