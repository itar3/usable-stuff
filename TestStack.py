class Stack:
    def __init__(self, size):
        self.array = [None]*size
        self.top = -1
        self.size = size
        self.count = 0

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        self.count == self.size

    def push(self, item):
        self.top +=1
        self.array[self.top] = item
        self.count+=1

    def pop(self):
        if stack.is_empty():
            raise IndexError("Stack is Empty")
        item = self.array[self.top]
        self.top -=1
        self.count -=1

        return item


stack = Stack(10)

stack.push(10)
stack.push(15)

print(stack.array)
print(stack.count)
stack.pop()
print(stack.array)
print(stack.count)
stack.pop()
stack.pop()