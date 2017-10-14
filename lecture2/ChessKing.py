x = int(input())
y = int(input())

a = int(input())
b = int(input())

if (x - 1 == a or x + 1 == a or x == a) and\
        (y - 1 == b or y + 1 == b or y == b):
    print("YES")
else:
    print("NO")
