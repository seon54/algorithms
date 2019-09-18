"""
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

<입력>
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

<출력>
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

"""

import sys


class Queue(object):

    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):

        if len(self.queue):
            value = self.queue[0]
            del self.queue[0]
            print(value)
        else:
            print(-1)

    def size(self):
        print(len(self.queue))

    def empty(self):
        print(0 if len(self.queue) else 1)

    def front(self):
        print(self.queue[0] if len(self.queue) else -1)

    def back(self):
        print(self.queue[-1] if len(self.queue) else -1)


num = int(sys.stdin.readline())
my_queue = Queue()

for i in range(num):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        my_queue.push(cmd[1])
    elif cmd[0] == 'pop':
        my_queue.pop()
    elif cmd[0] == 'size':
        my_queue.size()
    elif cmd[0] == 'empty':
        my_queue.empty()
    elif cmd[0] == 'front':
        my_queue.front()
    elif cmd[0] == 'back':
        my_queue.back()
