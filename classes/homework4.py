def file_type(s):
    index = s.rfind('.')
    if index == -1 or s[index + 1:] == '':
        return ''
    else:
        return s[index + 1:]

print(file_type('foo.doc'))