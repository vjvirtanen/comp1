words = []
indices = []
while (word := input('word: ')) != '!':
    words.append(word)

while (index := int(input('index: '))) >= 0:
    indices.append(index)

print(words)
print(indices)
for n in indices:
    words.pop(n)
print(words)