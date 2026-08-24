highest = 0 
for t in range(1, 101):
    change = (t - 1)*((t - 1) - 20)*((t - 1) - 100) - t*(t - 20)*(t - 100)
    if change > highest:
        highest = change
        time = t

print(time)