x = int(input())
y = int(input())

a = int(input())
b = int(input())

if ((x + y) % 2 == 0) and ((a + b) % 2 == 0):
    print("YES")
elif ((x + y) % 2 != 0) and ((a + b) % 2 != 0):
    print("YES")
else:
    print("NO")
