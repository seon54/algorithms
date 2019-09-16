"""
memory: 30016 kb
time: 4368 ms

"""

times = int(input())
stack = []
last = 0
result = ''
found = True

for i in range(times):
    num = int(input())

    while num > last:
        last += 1
        stack.append(last)
        result += '+'

    if stack[-1] == num:
        stack.pop()
        result += '-'
    else:
        found = False

if found:
    for s in result:
        print(s)
else:
    print('NO')
