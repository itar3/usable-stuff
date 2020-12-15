class Node:
    def __init__(self,item,next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def push(self,item):
        new_node = Node(item,self.top)
        self.top = new_node
        self.count+=1

    def pop(self):
        item = self.top.item
        self.top = self.top.next
        self.count-=1
        return item

s = Stack()
s.push(15)
s.push(25)
print(s.top.item)
s.pop()
print(s.top.item)
