class Node:
  def __init__(self, item, next):
    self.item =item
    self.next=next

class HashTableSeparateChaining:
    def __init__(self, size=3817):
        self.count = 0
        self.table_size = size
        self.array = [None] * self.table_size

    def __len__(self):
        return self.count

    def hash_function(self, key):
        h = 0
        a = 3711
        for i in range(len(key)):
            h = (h * a + ord(key[i])) % self.table_size
        return h

    def __setitem__(self, key, data):
        index = self.hash_function(key)

        if self.array[index] is None:
            head = Node((key, data), None)
            self.array[index] = head
            self.count += 1
            return
        else:
            current = self.array[index]
            while current is not None:
                if current.item[0] == key:
                    current.item = (key, data)
                    return
                current = current.next

            self.array[index] = Node((key, data), self.array[index])
            self.count += 1
            return

    def __getitem__(self, key):
        index = self.hash_function(key)

        if self.array[index] is None:
            raise Exception("key not exist")
        else:
            current = self.array[index]
            while current is not None:
                if current.item[0] == key:
                    return current.item[1]
                current = current.next
            raise Exception("key not found")


HT = HashTableSeparateChaining(1)
HT["FIT1008"] = "Intro to CS"
HT["FIT2004"] = "ADS"
# HT.insert("FIT1008", "Intro to CS")
# HT.insert("FIT2004", "ADS")

print(len(HT))
print(HT["FIT2004"])







