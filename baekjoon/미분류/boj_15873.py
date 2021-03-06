import sys


n = sys.stdin.readline().rstrip()

if len(n) > 2 and n[-2:] == '10':    
    a, b = map(int, [n[:-2], n[-2:]])    
else:
    a, b = map(int, [n[:-1], n[-1:]])
    
print(a+b)
