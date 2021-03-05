"""
str1, str2가 주어졌을 때 str1을 str2와 동일하게 만들기 위한 연산은 3가지 이다.
    1. 삽입
    2. 삭제
    3. 치환
두 단어 간의 교정 비용은 한 단어에서 다른 단어로 바꾸는 데 필요한 글자 연산의 횟수로 정의한다.
"""

# 재귀 O(3^n)

def edit_distance(str1, str2):

    if str1 is None or str1 == '': return len(str2)

    if str2 is None or str2 == '': return len(str1)

    if str1[0] == str2[0]:
        return edit_distance(str1[1:], str2[1:])

    remove_cnt = edit_distance(str1[1:], str2)
    replace_cnt = edit_distance(str1[1:], str2[1:])
    insert_cnt = edit_distance(str1, str2[1:])

    # 삭제, 치환, 삽입 연산에 상관없이 연산을 수행했으므로 마지막에 1을 더한 값을 반환
    return min(remove_cnt, replace_cnt, insert_cnt) + 1


print(edit_distance('support', 'sport'))

# DP

def edit_distance_dp(str1, str2):
    m, n = len(str1), len(str2)
    arr = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 제일 위의 행, str1 이 빈 문자열일 때 최소 교정 비용
    for i in range(n + 1):
        arr[0][i] = i

    # 제일 왼쪽 열, str2 이 빈 문자열일 때 최소 교정 비용
    for i in range(m + 1):
        arr[i][0] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):            
            
            # 두 글자가 같을 경우
            if str1[i - 1] == str2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1]
            else:
                arr[i][j] = min(arr[i][j - 1], arr[i - 1][j], arr[i - 1][j - 1]) + 1

    return arr[m][n]


print(edit_distance_dp('sunday', 'saturday'))