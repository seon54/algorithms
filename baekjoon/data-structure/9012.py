n = int(input())

for _ in range(n):
    data = list(input())
    stack = []

    while data:
        x = data.pop(0)

        if x == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(x)
        

    if stack:
        print('NO')
    else:
        print('YES')

######################################################################

for _ in range(n):
    data = list(input())
    sum_ = 0

    for s in data:
        if s == '(':
            sum_ += 1
        else:
            sum_ -= 1

        if sum_ < 0:
            print('NO')
            break

    if sum_:
        print('NO')
    else:
        print('YES')
