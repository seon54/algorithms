"""
01. 기본 자료구조 - 01. 기초 문제풀이
난이도: 하
유형: 배열, 완전 탐색
추천 풀이 시간: 20분
"""
import sys


n, m = list(map(int, sys.stdin.readline().split()))
cards = list(map(int, sys.stdin.readline().split()))

value = 0
length = len(cards)

for i in range(length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            temp = cards[i] + cards[j] + cards[k]
            if temp <= m:
                value = max(temp, value)

print(value)