class Node:
  def __init__(self, item, next):
    self.item =item
    self.next=next

class MyList:
    def __init__(self, size):
        self.count = 0
        # self.array = build_array(size)
        self.head = None

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return False

    def _get_node(self, index):
        assert 0 <= index < self.count, "index out of bound"
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def insert(self, index, item):
        if self.is_full():
            return False
        if index == 0:
            self.head = Node(item, self.head)
        else:
            node = self._get_node(index - 1)
            node.next = Node(item, node.next)
        self.count += 1
        return True

    def delete(self, index):
        valid_index = index >= 0 and index < self.count
        if self.is_empty():
            return False
        if valid_index:
            if index == 0:
                self.head = self.head.next
            else:
                node = self._get_node(index - 1)
                node.next = node.next.next
            self.count -= 1

        return valid_index

    def __str__(self):
        ret = ""

        current = self.head
        while current is not None:
            ret = ret + str(current.item) + ","
            current = current.next
        return ret

    def __len__(self):
        return self.count

    def __contains__(self, item):
        for i in range(self.count):
            if self.array[i] == item:
                return True
        return False


mylist = MyList(6)
print(mylist.insert(0, 2))
print(mylist.insert(0, 3))
print(mylist.insert(1, 4))
print(mylist.insert(2, 5))
print(mylist.delete(2))
print(mylist.delete(1))

print(str(mylist))


"""
mylist.print_all()
print(len(mylist))

print(8 in mylist)
"""
# mylist[2] =3
