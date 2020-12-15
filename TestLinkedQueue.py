class Node:
    def __init__(self,item,next):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def append(self,item):
        new_node = Node(item, None)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.count+=1

    def serve(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        item = self.front.item
        self.front = self.front.next
        if self.is_empty():
            self.rear = None
        self.count -=1
        return item
