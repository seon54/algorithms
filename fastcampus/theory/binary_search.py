# 정렬이 된 탐색 자료를 둘로 나누어 탐색

def binary_search(arr, value):
    
    if len(arr) == 1 and arr[0] == value:
        return True
    if len(arr) == 1 and arr[0] != value:
        return False

    mid = len(arr) // 2

    if arr[mid] == value:
        return True
    elif arr[mid] < value:
        return binary_search(arr[mid:], value)
    else:
        return binary_search(arr[:mid], value)


import random

data = [5, 19, 26, 28, 31, 38, 56, 71, 89, 98]

print(binary_search(data, 7))


    