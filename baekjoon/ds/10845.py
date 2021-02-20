import sys


class Queue:

    def __init__(self):
        self.queue = []
        self.length = 0

    def push(self, data):
        self.queue.append(data)
        self.length += 1

    def pop(self):
        if self.queue:
            x = self.queue[0]
            del self.queue[0]
            self.length -= 1
            print(x)
        else:
            print(-1)

    def size(self):
        print(self.length)

    def empty(self):
        print(0 if self.length else 1)

    def front(self):
        print(self.queue[0] if self.queue else -1)

    def back(self):
        print(self.queue[-1] if self.queue else -1)

n = int(sys.stdin.readline())
queue = Queue()

while n:
    n -= 1
    cmd = sys.stdin.readline().strip().split()

    if cmd[0] == 'push':
        queue.push(cmd[1])
    elif cmd[0] == 'pop':
        queue.pop()
    elif cmd[0] == 'size':
        queue.size()
    elif cmd[0] == 'empty':
        queue.empty()
    elif cmd[0] == 'front':
        queue.front()
    elif cmd[0] == 'back':
        queue.back()