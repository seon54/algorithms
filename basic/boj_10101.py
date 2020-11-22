import sys


a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
sum_ = a + b + c


if sum_ != 180:
    print('Error')
elif a == b == c == 60:
    print('Equilateral')
elif a == b or b == c or a == c:
    print('Isosceles')
else:
    print('Scalene')