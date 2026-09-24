def uniques(numbers):
    for n in numbers:
        if numbers.count(n) > 1:
                return False
    return True

print(uniques([1,2,3,4,4]))