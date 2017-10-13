a = int(input())
b = int(input())
n = int(input())

allCents = (a * 100 + b) * n
rub = allCents // 100
cents = allCents % 100

print(rub, cents, sep=' ', end='')
