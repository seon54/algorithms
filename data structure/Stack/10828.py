'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

<입력>
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
<출력>
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
'''

# 첫번째

# class Stack:
#
#     def __init__(self):
#         self.items = []
#
#     def push(self, x):
#         self.items.append(x)
#
#     def pop(self):
#         if len(self.items) > 0:
#             print(self.items[-1])
#             del self.items[-1]
#         else:
#             print(-1)
#
#     def size(self):
#         print(len(self.items))
#
#     def empty(self):
#         if len(self.items):
#             print(1)
#         else:
#             print(0)
#
#     def top(self):
#         if len(self.items) > 0:
#             print(self.items[-1])
#         else:
#             print(-1)
#
#
# cmd_times = int(input())
# st = Stack()
#
# for i in range(cmd_times):
#     cmds = input().split()
#     cmd = cmds[0]
#
#     if cmd == 'pop':
#         st.pop()
#     elif cmd == 'size':
#         st.size
#     elif cmd == 'empty':
#         st.empty()
#     elif cmd == 'top':
#         st.top()
#     elif cmd == 'push':
#         st.push(int(cmds[-1]))

# 두번째
import sys

class Stack2:
    def __init__(self):
        self.items = []
        self.length = 0

    def push(self, value):
        self.items.append(value)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return -1
        last = self.items[-1]
        del self.items[-1]
        self.length -= 1
        return last

    def size(self):
        return self.length

    def empty(self):
        return 1 if self.length == 0 else 0

    def top(self):
        return self.items[-1] if self.length > 0 else -1

times = int(input())
st = Stack2()

while times:
    times -= 1
    cmds = sys.stdin.readline().split()
    cmd = cmds[0]
    if cmd == 'push':
        st.push(cmds[-1])
    elif cmd == 'pop':
        print(st.pop())
    elif cmd == 'size':
        print(st.size())
    elif cmd == 'empty':
        print(st.empty())
    elif cmd == 'top':
        print(st.top())
    else:
        print('False')
