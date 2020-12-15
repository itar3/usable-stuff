class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class MyStack:
    def __init__(self, size):
        if size <= 0:
            raise Exception("size must be positive")
        self.count = 0
        self.top = None

    def is_full(self):
        return False

    def is_empty(self):
        return self.top is None

    def push(self, item):
        if self.is_full():
            raise Exception("stack is full")
        self.top = Node(item, self.top)
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")
        tobereturn = self.top.item
        self.top = self.top.next
        self.count -= 1
        return tobereturn

    def __len__(self):
        return self.count


mystack = MyStack(6)
mystack.push(4)
mystack.push(2)
mystack.push(1)
mystack.push(6)
mystack.push(7)
mystack.push(7)

print(mystack.pop())
print(mystack.pop())

name = "fermi"
mystack2 = MyStack(len(name))
for i in range(len(name)):
    mystack2.push(name[i])
ret = ""

while not mystack2.is_empty():
    ret = ret + mystack2.pop()

print(ret)
