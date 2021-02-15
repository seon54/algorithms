"""
10. 고급 탐색 알고리즘
문제: 트리의 높이와 너비
난이도: 중
유형: 트리, 구현
추천 풀이 시간: 50분
"""
#  틀림

# from collections import defaultdict

# class Node:
#     def __init__(self, data, left, right, level=None):
#         self.data = data
#         self.left = left
#         self.right = right      

        
# def inorder(node, array, level):
#     level += 1

#     if node.left != -1:    
#         inorder(tree[node.left], array, level)

#     if node.data != -1:
#         array.append((node.data, level))

#     if node.right != -1:
#         inorder(tree[node.right], array, level)

#     return array

# n = int(input())
# tree = dict()
# node = []

# for i in range(n):
#     data, left, right = list(map(int, input().split(' ')))
#     tree[data] = Node(data, left, right, i)

# level_dict = defaultdict(list)
# result = inorder(tree[1], node, 0)

# for i in range(len(result)):
#     level = result[i][1]
#     level_dict[level].append(i + 1)

# max_width = 0
# result_level = 0

# for level, index_list in level_dict.items():    
#     min_ = min(index_list)
#     max_ = max(index_list)
#     if max_ - min_ + 1 >= max_width:
#         max_width = max_ - min_ + 1
#         if level < result_level:
#             result_level = level

# print(result_level, max_width)

####################################################################################

class Node:
    def __init__(self, data, left, right):
        self.parent = -1
        self.data = data
        self.left = left
        self.right = right

def inorder(node, level):
    global level_depth, x
    level_depth = max(level_depth, level)

    if node.left != -1:
        inorder(tree[node.left], level + 1)

    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)

    x += 1

    if node.right != -1:
        inorder(tree[node.right], level + 1)


n = int(input())
tree = {}
level_min, level_max = [n], [0]
root = -1
x = 1
level_depth = 1

# 초기화
for i in range(1, n + 1):
    tree[i] = Node(i, -1, -1)
    level_min.append(n)
    level_max.append(0)

for _ in range(n):
    data, left, right = map(int, input().split())
    tree[data].left = left
    tree[data].right = right
    if left != -1:
        tree[left].parent = data
    if right != -1:
        tree[right].parent = data

for i in range(1, n + 1):
    if tree[i].parent == -1:
        root = i

inorder(tree[root], 1)
        
result_level = 1
result_width = level_max[1] - level_min[1] + 1

for i in range(2, level_depth + 1):
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i
        result_width = width

print(result_level, result_width)