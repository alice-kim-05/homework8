X = int(input())
for i in range(1, X+1):
    summa = 0
    for n in range(1, i + 1):
        summa += n
    print(summa)
