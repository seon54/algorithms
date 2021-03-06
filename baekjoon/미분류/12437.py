#  41

t = int(input())

for i in range(t):
    month, days, weekdays = map(int, input().split())
    total = month * days
    cnt, mod = 0, 0

    while total:
        total -= days

        if mod:
            cnt += 1
            temp = days - mod
        else:
            temp = days

        lines = temp // weekdays
        mod = 0

        if temp % weekdays:
            lines += 1
            mod = lines * weekdays - temp
        
        cnt += lines
    
    print(f'Case #{i + 1}: {cnt}')
            