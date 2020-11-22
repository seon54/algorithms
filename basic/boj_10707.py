import sys


a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
p = int(sys.stdin.readline())

x = a * p
y = b if p <= c else b + (p - c) * d

print(min([x, y]))