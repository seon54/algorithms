import sys


text = list(sys.stdin.readline().strip())
temp = list()
m = int(sys.stdin.readline())

for _ in range(m):
    c = sys.stdin.readline().strip().split()

    if c[0] == 'P':
        text.append(c[1])
    elif c[0] == 'L':
        if text:
            temp.append(text.pop())
    elif c[0] == 'D':
        if temp:
            text.append(temp.pop())
    elif c[0] == 'B':
        if text:
            text.pop()

text.extend(temp[::-1])

print(''.join(text))