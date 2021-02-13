class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        head = self.head
        while True:
            if value < head.value:
                if head.left:
                    head = head.left
                else:
                    head.left = Node(value)
                    break
            else:
                if head.right:
                    head = head.right
                else:
                    head.right = Node(value)
                    break

    def search(self, value):
        head = self.head
        while head:
            if head.value == value:
                return True
            elif value < head.left.value:
                head = head.left
            else:
                head = head.right
        return False

    def delete(self, value):
        
        # 삭제할 노드 찾기
        searched = False
        node = self.head
        parent = self.head

        while node:
            if node.value == value:
                searched = True
                break
            elif value < node.value:
                node = node.left
            else:
                node = node. right

        if not searched:
            return False

        # 자식 노드가 없을 때
        if not node.left and not node.right:
            if value < parent.value:
                parent.left = None
            else:
                parent.right = None
            
        # 자식 노드가 1개일 때 (왼쪽)
        elif node.left and not node.right:
            if value < parent.value:
                parent.left = node.left
            else:
                parent.right = node.left
        
        # 자식 노드가 1개일 때 (오른쪽)
        elif node.right and not node.left:
            if value < parent.value:
                parent.left = node.right
            else:
                parent.right = node.right

        # 자식 노드가 2개일 때
        elif node.left and node.right:
            change_node = node
            change_parent = node
            while change_node.left:
                change_parent = change_node
                change_node = change_node.left
            if change_node.right:
                change_parent.left = change_node.right
            else:
                change_parent.left = None

            parent.right = change_node
            change_node.left = node.left
            change_node.right = node.right


        

        