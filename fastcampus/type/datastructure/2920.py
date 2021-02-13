"""
01. 기본 자료구조 - 01. 기초 문제풀이
난이도: 하
문제 유형: 배열, 구현
추천 풀이 시간: 15
"""

import sys


def solution1():
    input_list = list(map(int, sys.stdin.readline().split()))
    ascending_nums = [i for i in range(1, 9)]
    is_ascending = True
    is_descending = True

    for i in range(len(input_list)):
        if input_list[i] != ascending_nums[i]:
            is_ascending = False

    for i in range(len(input_list)):
        if input_list[i] != ascending_nums[-1 - i]:
            is_descending = False

    if is_ascending:
        print('ascending')
    elif is_descending:
        print('descending')
    else:
        print('mixed')


def solution2():
    a = list(map(int, sys.stdin.readline().split()))
    ascending = True
    descending = True
    for i in range(1, 8):
        if a[i] > a[i - 1]:
            descending = False
        elif a[i] < a[i - 1]:
            ascending = False
    
    if ascending:
        print('ascending')
    elif descending:
        print('descending')
    else:
        print('mixed')

    