"""
동적계획법 - 06.문제풀이

https://www.acmicpc.net/problem/12849
본대 산책

0 정보
1 전산
2 미래
3 신앙
4 한경
5 진리
6 학생
7 형남
"""
# 주어진 시간에 각 위치에 갈 수 있는 수
dp = [0] * 8
dp[0] = 1


def nxt(dp_list):
    temp = [0] * 8
    temp[0] = dp_list[1] + dp_list[2]
    temp[1] = dp_list[0] + dp_list[2] + dp_list[3]
    temp[2] = dp_list[0] + dp_list[1] + dp_list[3]
    temp[3] = dp_list[1] + dp_list[2] + dp_list[4] + dp_list[5]
    temp[4] = dp_list[2] + dp_list[3] + dp_list[5] + dp_list[7]
    temp[5] = dp_list[3] + dp_list[4] + dp_list[6]
    temp[6] = dp_list[5] + dp_list[7]
    temp[7] = dp_list[4] + dp_list[6]

    for i in range(8):
        temp[i] %= 1000000007

    return temp

for i in range(int(input())):
    dp = nxt(dp)

print(dp[0])

