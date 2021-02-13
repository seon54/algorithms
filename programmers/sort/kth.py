def solution(array, commands):
    answer = []
    
    for c in commands:
        i = c[0] - 1
        j = c[1]
        k = c[2] - 1
        l = array[i:j]
        l.sort()
        answer.append(l[k])        
        
    return answer


def solution2(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
