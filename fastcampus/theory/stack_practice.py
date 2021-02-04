class Stack:

    def __init__(self):
        self.stack_list = list()

    def push(self, data):
        self.stack_list.append(data)

    def pop(self):
        if self.stack_list:
            data = self.stack_list[-1]
            del self.stack_list[-1]
            return data
        else:
            return

stack = Stack()
print(stack.pop())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())