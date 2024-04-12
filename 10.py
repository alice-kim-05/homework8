N = int(input())
for i in range(1, N+1):
    summa = 0
    for n in range(1, (i // 2) + 1):
        if i % n == 0:
            summa += n
    if summa == i:
        print(i)
