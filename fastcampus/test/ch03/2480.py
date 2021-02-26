array = list(map(int, input().split()))
length = len(set(array))

if length == 1:
    print(array[0] * 1000 + 10000)
elif length == 2:
    array.sort()
    print(array[1] * 100 + 1000)
else:
    print(max(array) * 100)

######################################################

lst = sorted(list(map(int, input().split())))

if len(set(lst)) == 1:
    print(10000 + lst[0] * 1000)
elif len(set(lst)) == 2:
    print(1000 + lst[1] * 100)
else:
    print(lst[2] * 100)