class Node:
  def __init__(self, item, next):
    self.item =item
    self.next=next

class MyQueue:
    def __init__(self, size):
        if size <= 0:
            raise Exception("size must be positive")
        self.count = 0
        self.front = None
        self.rear = None

    def is_full(self):
        return False

    def is_empty(self):
        return self.front is None

    def append(self, item):
        temp = Node(item, None)
        if self.is_empty():
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self.count += 1

    def serve(self):
        if self.is_empty():
            raise Exception("queue is empty")
        tobereturn = self.front.item
        self.front = self.front.next
        self.count -= 1
        return tobereturn


myqueue = MyQueue(5)
myqueue.append(5)
myqueue.append(1)
myqueue.append(3)
print(myqueue.serve())
print(myqueue.serve())
print(myqueue.serve())


