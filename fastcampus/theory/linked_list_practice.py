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

    def printAll(self):
        node = self
        while node.next:
            print(node.data)
            node = node.next

        


node1 = Node(1)

for i in range(2, 5):
    node1.add(i)

node2 = Node(1.4)

head = node1
search = True
while search:
    if head.data < node2.data:
        search = False
        break
    head = head.next

head.next, node2.next = node2, head.next

node1.printAll()