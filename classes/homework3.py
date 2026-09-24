def dashify_substring(s, sub):

    return s.replace(sub, '-' + sub + '-', 1)
    

print(dashify_substring('foo', 'o'))

