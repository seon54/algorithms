"""
10. 고급 탐색 알고리즘
문제: 트리 순회
난이도: 하
유형: 트리, 구현
추천 풀이 시간: 20분

** 반드시 기억
** 재귀
"""

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def pre_order(node):
    print(node.data, end='')
    if node.left != '.':
        pre_order(tree[node.left])
    if node.right != '.':
        pre_order(tree[node.right])

def in_order(node):
    if node.left != '.':
        in_order(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        in_order(tree[node.right])

def post_order(node):
    if node.left != '.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.data, end='')

n = int(input())
tree = dict()
for i in range(n):
    data, left, right = input().split()
    tree[data] = Node(data, left, right)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
        
