import sys


class Deque:

    def __init__(self):
        self.deque = []
        self.length = 0

    def push_front(self, data):
        self.deque.insert(0, data)
        self.length += 1

    def push_back(self, data):
        self.deque.append(data)
        self.length += 1

    def pop_front(self):
        if self.deque:
            x = self.deque[0]
            del self.deque[0]
            self.length -= 1
            print(x)
        else:
            print(-1)

    def pop_back(self):
        if self.deque:
            x = self.deque[-1]
            del self.deque[-1]
            self.length -= 1
            print(x)
        else:
            print(-1)

    def size(self):
        print(self.length)

    def empty(self):
        print(0 if self.length else 1)

    def front(self):
        if self.length:
            print(self.deque[0])
        else:
            print(-1)

    def back(self):
        if self.length:
            print(self.deque[-1])
        else:
            print(-1)


n = int(sys.stdin.readline())
deque = Deque()

for _ in range(n):
    cmd = sys.stdin.readline().strip().split()

    if cmd[0] == 'push_front':
        deque.push_front(cmd[1])
    elif cmd[0] == 'push_back':
        deque.push_back(cmd[1])
    elif cmd[0] == 'pop_front':
        deque.pop_front()
    elif cmd[0] == 'pop_back':
        deque.pop_back()
    elif cmd[0] == 'size':
        deque.size()
    elif cmd[0] == 'empty':
        deque.empty()
    elif cmd[0] == 'front':
        deque.front()
    elif cmd[0] == 'back':
        deque.back()