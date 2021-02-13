"""
03. 고급 자료구조
난이도: 중
유형: 해시, 집합, 그래프
추천 풀이 시간: 50분

민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 
우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.
어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

[입력]
첫째 줄에 테스트 케이스의 개수가 주어진다. 
각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 
다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 
친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

[출력]
친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
"""
from collections import defaultdict
import sys


t = int(sys.stdin.readline())

for _ in range(t):

    f = int(sys.stdin.readline())
    friends = defaultdict(set)

    for _ in range(f):
        a, b = list(sys.stdin.readline().split())
        
        friends[a].update([a, b])
        friends[b].update([a, b])

        friends[a].update(friends[b])
        friends[b].update(friends[a])

        a_cnt = len(friends[a])
        b_cnt = len(friends[b])

        print(max(a_cnt, b_cnt))

# 시간초과

# Union-Find


def find_ex(x):
    if x == parent[x]:
        return x
    else:
        p = find_ex(parent[x])
        parent[x] = p
        return parent[x]


def union_ex(x, y):
    x = find_ex(x)
    y = find_ex(y)

    # 왼쪽값을 부모로 설정
    parent[y] = x

parent = []

for i in range(0, 5):
    parent.append(i)

union_ex(1, 4)
union_ex(2, 4)

for i in range(1, len(parent)):
    print(find_ex(i), end=' ')


########################################################################


def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

t = int(input())

for _ in range(t):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            parent[y] = 1
        
        union(x, y)

        print(number[find(x)])