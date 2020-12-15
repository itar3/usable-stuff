class Queue:
    def __init__(self,size):
        self.array = [None]*size
        self.front = 0
        self.rear = 0
        self.count = 0

    def is_empty(self):
        return (self.count == 0)

    def append(self,item):
        self.array[self.rear] = item
        self.count+=1
        self.rear+=1

    def serve(self):
        item = self.array[self.front]
        self.front+=1
        self.count-=1
        return item



q = Queue(10)

q.append(15)
q.append(255)
print(q.array)
q.serve()
t = q.serve()
print(t)
print(q.rear)
print(q.front)