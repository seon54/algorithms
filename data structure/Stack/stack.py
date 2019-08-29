class Stack(object):
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return not bool(self.items)
    
    def push(self, value):
        self.items.append(value)
        
    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print('Stack is empty')
            
    def size(self):
        return len(self.items)
    
    def top(self):
        if self.items:
            return self.items[-1]
        else:
            print('Stack is empty')
            
    def __repr__(self):
        return repr(self.items)
    
# stack with node

class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer
     
        
class Stack2(object):
    def __init__(self):
        self.head = None
        self.count = 0
        
    def isEmpty(self):
        return not bool(self.head)
    
    def push(self, item):
        self.head = Node(item, self.head)
        self.count += 1
        
    def pop(self):
        if self.count > 0 and self.head:
            node = self.head
            self.head = node.pointer
            self.count -= 1
            return node.value
        else:
            print('Stack is empty')
            
    def top(self):
        if self.count > 0 and self.head:
            return self.head.value
        else:
            print('Stack is empty')
            
    def size(self):
        return self.count
    
    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()
