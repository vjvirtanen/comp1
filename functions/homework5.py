def remove(orig, x, out):
    out.clear()
    out += [n for n in orig if n != x]
    out += [0] * (len(orig) - len(out))

    

orig = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
x = 4
out = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

remove(orig, x, out)

print("ORIG:", orig)
print("X:", x)
print("OUT:", out)


