x = int(input())

lastDigit = x % 10
x -= lastDigit
print(int(x / 10))
