st = '123456789'
for i in range(0, 8+1):
    k = int(st[:i+1]) * 8 + int(st[i])
    print(f'{st[:i+1]} * 8 + {st[i]} = {k}')
for n in range(0, 8+1):
    l = int(st[:n+1]) * 9 + int(st[n]) + 1
    print(f'{st[:n+1]} * 9 + {int(st[n]) + 1} = {l}')
for m in range(1, 9+1):
    o = int('1' * m) * int('1' * m)
    print('1' * m, '*', '1' * m, '=', o)
