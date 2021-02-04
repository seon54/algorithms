import queue

# basic queue
q1 = queue.Queue()
q1.put(1)
q1.put(2)
print(q1.qsize())
print(q1.get())

print("=============")

# LIFO queue
q2 = queue.LifoQueue()
q2.put("a")
q2.put("b")
q2.put("c")
print(q2.qsize())

while not q2.empty():
    print(q2.get())

print("=============")

# Priority Queue
q3 = queue.PriorityQueue()
q3.put((10, 'apple'))
q3.put((20, 'banana'))
q3.put((15, 'chicken'))
print(q3.qsize())

while not q3.empty():
    print(q3.get())

print("=============")

# Implement queue

class MyQueue:

    def __init__(self):
        self.queue_list = list()

    def enqueue(self, data):
        self.queue_list.append(data)

    def dequeue(self):
        if self.queue_list:
            data = self.queue_list[0]
            del self.queue_list[0]
            return data
        else:
            return None

q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
