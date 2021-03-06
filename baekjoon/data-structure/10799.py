stick = input().strip()
stack = []
cnt = 0

for i in range(len(stick)):

    if stick[i] == '(':
        stack.append(stick[i])
    else:   # ) 일 때
        if stick[i - 1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)