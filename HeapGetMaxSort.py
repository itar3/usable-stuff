class Heap:
    def __init__(self):
        self.count = 0
        self.array = [None] * 100

    def is_empty(self):
        return self.count == 0

    def add(self, key, value):
        item = (key, value)
        if self.count + 1 < len(self.array):
            self.array[self.count + 1] = item
        else:
            raise Exception("Heap is full")
        self.count += 1
        self.rise(self.count)

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def rise(self, node):
        while node > 1 and self.array[node][0] > self.array[node // 2][0]:
            print('rise')
            self.swap(node, node // 2)
            node = node // 2

    def get_max(self):
        tobereturned = self.array[1][0]
        self.swap(1, self.count)
        self.count -= 1
        self.sink(1)
        return tobereturned

    def sink(self, node):
        while 2 * node <= self.count:
            print('sink')
            child = self._get_largest_child(node)
            if self.array[child] < self.array[node]:
                break
            self.swap(child, node)
            node = child

    def _get_largest_child(self, node):
        if node * 2 == self.count or self.array[node * 2] > self.array[2 * node + 1]:
            return 2 * node
        else:
            return 2 * node + 1


myheap = Heap()
myheap.add(5, "test")
myheap.add(3, "test1")
myheap.add(1, "test3")
myheap.add(4, "tes5")
myheap.add(6, "tes8")
myheap.add(10, "test9")

for i in range(myheap.count + 1):
    print(myheap.array[i])

print(myheap.get_max())

# for i in range(myheap.count + 1):
#     print(myheap.array[i])
#
# print(myheap.get_max())
#
# for i in range(myheap.count + 1):
#     print(myheap.array[i])
#
# alist = [2, 8, 4, 4, 7, 9, 3, 2, 9]
#
#
# def heapsort(alist):
#     heap = Heap()
#     for item in alist:
#         heap.add(item, "value")
#
#     temp = []
#     for i in range(len(alist)):
#         temp.append(heap.get_max())
#
#     return temp
#
#
# print(heapsort(alist))


