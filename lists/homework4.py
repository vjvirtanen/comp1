words1 = []
while len(a := input('word: ')) != 1:
    words1.append(a)

while len(a := input('word: ')) != 1:
    if a in words1:
        print(words1.index(a))