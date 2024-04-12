N = int(input())
for i in range(2, N + 1):
    k = 0
    for n in range(1, (i // 2) + 1):
        if i % n == 0:
            k += 1
        if k > 1:
            break
    if k == 1:
        print(i)
