def max_char_rep(s):
    longest = 0
    current = 0 
    previous = ''

    for char in s:
        if char == previous:
            current += 1
        else:
            current = 1
            previous = char

        if current > longest:
            longest = current

    return longest

print(max_char_rep(''))