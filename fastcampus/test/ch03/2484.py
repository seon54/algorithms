n = int(input())
nums = []

for _ in range(n):
    array = sorted(list(map(int, input().split())))
    length = len(set(array))

    if length == 1:
        nums.append(50000 + array[0] * 5000)
    elif length == 2:
        if array[1] == array[2]:
            nums.append(10000 + array[1] * 1000)
        else:
            nums.append(2000 + array[0] * 500 + array[2] * 500)        
    elif length == 3:
        d = {array.count(x): x for x in array}
        nums.append(1000 + d[2] * 100)
    else:
        nums.append(max(array) * 100)

print(max(nums))

####################################################################################

def money():
    lst = sorted(list(map(int, input().split())))
    
    if len(set(lst)) == 1:
        return lst[0] * 5000 + 50000

    if len(set(lst)) == 2:
        if lst[1] == lst[2]:
            return 10000 + lst[1] * 1000
        else:
            return 2000 + (lst[1] + lst[2]) * 500
    
    for i in range(3):
        if lst[i] == lst[i + 1]:
            return 1000 + lst[i] * 100
    
    return lst[-1] * 100


N = int(input())

print(max(money() for i in range(N)))