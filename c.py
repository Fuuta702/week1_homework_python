sosuu = []

for num in range(2, 41):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1

    if count == 0:
        sosuu.append(num)

print(sosuu)
