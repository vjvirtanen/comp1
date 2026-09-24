def alternate(lst):
    alternated = []
    start = 0
    end = len(lst)

    for _ in range(end // 2):
        alternated.append(lst[start])
        alternated.append(lst[end - 1])
        start += 1
        end -= 1

    if len(lst) % 2 != 0:
        alternated.append(lst[start])

    return alternated