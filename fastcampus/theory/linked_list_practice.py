class Node:

    def __init__(self, data, next=None):        
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def add(self, data):
        node = self
        while node.next:
            node = node.next
        node.next = Node(data)

class LinkedList:

    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
        else:
            self.head = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head:
            node = self.head

            # 첫번째 값 삭제할 경우
            if node.data == data:
                self.head = node.next
                del node

            # 중간, 마지막 값 삭제할 경우

            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next
        else:
            return

    def findData(self, data):
        if self.head:
            node = self.head
            while node:
                if node.data == data:
                    print(node.data)
                    break
                else:
                    node = node.next
        else:
            print("There is no data")
            return 
        

linked_list = LinkedList(1)

for i in range(2, 10):
    linked_list.add(i)

linked_list.desc()

print("=====================")

linked_list.delete(3)

linked_list.desc()

print("=====================")

linked_list.findData(5)