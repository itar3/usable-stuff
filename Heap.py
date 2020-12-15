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
        while node > 1 and self.array[node][0] < self.array[node // 2][0]:
            self.swap(node//2, node)
            node = node // 2

    def sink(self, node):

        while node*2 <= self.count:
            print('sink')
            child = self._get_smallest_child(node)
            print(child)
            if self.array[child] > self.array[node]:
                break
            self.swap(node, child)
            node = child

    def _get_smallest_child(self, node):
        if node * 2 == self.count or self.array[node * 2] < self.array[2 * node + 1]:
            return 2 * node
        else:
            return 2 * node + 1

    def get_min(self):
        retval = self.array[1]
        self.swap(1, self.count)
        self.count -= 1
        self.sink(1)

        return retval



myheap = Heap()
myheap.add(6, "test")
myheap.add(5, "test1")
myheap.add(3, "test3")
myheap.add(1, "tes5")
myheap.add(4, "tes5")
myheap.add(2, "tes5")




for i in range(myheap.count + 1):
    print(myheap.array[i])

print('\n'
)

print(myheap.get_min())
for i in range(myheap.count + 1):
    print(myheap.array[i])



#
# print(myheap.get_min())
# for i in range(myheap.count + 1):
#     print(myheap.array[i])

