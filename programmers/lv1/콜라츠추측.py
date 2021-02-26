def solution(num):
    answer = 0
    
    while answer < 500:
        if num == 1:
            break
            
        if num % 2:
            num = num * 3 + 1
        else:
            num //= 2
        
        answer += 1
            
    return answer if answer != 500 else -1


def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1