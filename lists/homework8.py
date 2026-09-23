words = []
indices = []
nwords = []
while (word := input('word: ')) != '':
    words.append(word)

while (index := int(input('index: '))) >= 0:
    indices.append(index)

print(words)
print(indices)
for i in range(len(words)):
    if i not in indices:
        nwords.append(words[i])
print(nwords)