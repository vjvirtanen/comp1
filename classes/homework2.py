def date_of_birth(ssn):
    if ssn[6:7] == '+':
        century = '18'
    elif ssn[6:7] == '-':
        century = '19'
    elif ssn[6:7] == 'A':
        century = '20'

    y = century + ssn[4:6]

    

    return y

print(date_of_birth('070809A123'))