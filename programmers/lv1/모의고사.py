def solution(answers):
    first = [1,2,3,4,5] * (len(answers) // 5 + 1)
    second = [2,1,2,3,2,4,2,5] * (len(answers) // 8 + 1)
    third = [3,3,1,1,2,2,4,4,5,5] * (len(answers) // 10 + 1)
    cnt = [0 for _ in range(3)]
    answer = []
    
    for a, v in zip(answers, first):
        if a == v:
            cnt[0] += 1
            
    for a, v, in zip(answers, second):
        if a == v:
            cnt[1] += 1
            
    for a, v in zip(answers, third):
        if a == v:
            cnt[2] +=1
            
    for i, v in enumerate(cnt):
        if max(cnt) == v:
            answer.append(i + 1)
    return answer

###############################################################

def other(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
