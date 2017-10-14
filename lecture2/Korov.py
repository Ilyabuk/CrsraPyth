x = int(input())

if 10 < x < 20:
    print(x, "korov")
elif x % 10 == 1:
    print(x, "korova")
elif x % 10 == 2 or x % 10 == 3 or x % 10 == 4:
    print(x, "korovy")
else:
    print(x, "korov")
