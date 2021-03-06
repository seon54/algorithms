import sys


class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, data):
        self.stack.append(data)
        self.length += 1

    def pop(self):
        if self.stack:
            x = self.stack[-1]
            del self.stack[-1]
            self.length -= 1
            print(x)
        else:
            print(-1)

    def size(self):
        print(self.length)

    def empty(self):
        print(0 if self.length else 1)

    def top(self):
        if self.stack:
            print(self.stack[-1])
        else:
            print(-1)

n = int(sys.stdin.readline())
stack = Stack()

while n:
    n -= 1

    cmd = sys.stdin.readline().strip().split()

    if cmd[0] == 'push':
        stack.push(cmd[1])
    elif cmd[0] == 'pop':
        stack.pop()
    elif cmd[0] == 'top':
        stack.top()
    elif cmd[0] == 'size':
        stack.size()
    elif cmd[0] == 'empty':
        stack.empty()
