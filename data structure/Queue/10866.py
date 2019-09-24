import sys


class Deque:
    def __init__(self):
        self.deque = []

    def push_front(self, x):
        self.deque.insert(0, x)

    def push_back(self, x):
        self.deque.append(x)

    def pop_front(self):
        if len(self.deque):
            v = self.deque[0]
            del self.deque[0]
            print(v)
        else:
            print(-1)

    def pop_back(self):
        if len(self.deque):
            v = self.deque[-1]
            del self.deque[-1]
            print(v)
        else:
            print(-1)

    def size(self):
        print(len(self.deque))

    def empty(self):
        if self.deque:
            print(0)
        else:
            print(1)

    def front(self):
        if self.deque:
            print(self.deque[0])
        else:
            print(-1)

    def back(self):
        if self.deque:
            print(self.deque[-1])
        else:
            print(-1)


cnt = int(sys.stdin.readline())
d = Deque()

for i in range(cnt):
    cmd = sys.stdin.readline().strip().split()

    if cmd[0] == 'push_back':
        d.push_back(cmd[1])
    elif cmd[0] == 'push_front':
        d.push_front(cmd[1])
    elif cmd[0] == 'pop_front':
        d.pop_front()
    elif cmd[0] == 'pop_back':
        d.pop_back()
    elif cmd[0] == 'size':
        d.size()
    elif cmd[0] == 'empty':
        d.empty()
    elif cmd[0] == 'front':
        d.front()
    elif cmd[0] == 'back':
        d.back()