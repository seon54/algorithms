from collections import deque
import sys


n = int(sys.stdin.readline())
stack = deque(range(1, n + 1))

while len(stack) > 1:
    stack.popleft()
    stack.append(stack.popleft())

print(stack[0])