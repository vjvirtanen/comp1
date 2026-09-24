m = 0
nums = [3, 7, 4]
output = []
while m < len(nums):
    n = 0
    while n < len(nums):
        if not m == n:
            output.append(10*nums[m] + nums[n])
        n += 1
    m += 1

print(output)