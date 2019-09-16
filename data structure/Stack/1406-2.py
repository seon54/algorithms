import sys

left = list(sys.stdin.readline().strip())
right = []

cnt = int(sys.stdin.readline())

for _ in range(cnt):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'L':
        if left:
            right.append(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.pop())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])

right.reverse()
sys.stdout.write(''.join(left) + ''.join(right))
