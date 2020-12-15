class MyStack:
    def __init__(self, size):
        if size <= 0:
            raise Exception("size must be positive")
        self.count = 0
        self.top = -1
        self.array = [0] * size

    def is_full(self):
        return self.count >= len(self.array)

    def is_empty(self):
        return self.count == 0

    def push(self, item):
        if self.is_full():
            raise Exception("stack is full")
        self.top += 1
        self.array[self.top] = item
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")
        tobereturn = self.array[self.top]
        self.top -= 1
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


class MyQueue:
    def __init__(self, size):
        if size <= 0:
            raise Exception("size must be positive")
        self.count = 0
        self.front = 0
        self.rear = 0
        self.array = [0] * size

    def is_full(self):
        return self.rear >= len(self.array)

    def is_empty(self):
        return self.count == 0

    def append(self, item):
        if self.is_full():
            raise Exception("queue is full")
        self.array[self.rear] = item
        self.rear += 1
        self.count += 1

    def serve(self):
        if self.is_empty():
            raise Exception("queue is empty")
        tobereturn = self.array[self.front]
        self.front += 1
        self.count -= 1
        return tobereturn


myqueue = MyQueue(5)
myqueue.append(5)
myqueue.append(1)
myqueue.append(3)
print(myqueue.serve())
print(myqueue.serve())
print(myqueue.rear,myqueue.front, myqueue.count)
print(myqueue.array)