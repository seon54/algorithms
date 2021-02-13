def split(arr):
    if len(arr) <= 1:
        return arr    
    
    mid = len(arr) // 2
    left = split(arr[:mid])
    right = split(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    lp, rp = 0, 0

    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1

    while lp < len(left):
        result.append(left[lp])
        lp += 1

    while rp < len(right):
        result.append(right[rp])
        rp += 1

    return result
        
