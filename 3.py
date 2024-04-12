income = int(input())
summa = 0
k = 0
while income != 0:
    summa += income
    k += 1
    income = int(input())
print(summa/k)
