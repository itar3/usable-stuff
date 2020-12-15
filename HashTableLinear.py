class HashTableLinear:
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

        for _ in range(self.table_size):
            if self.array[index] is None:
                self.array[index] = (key, data)
                self.count += 1
                return
            elif self.array[index][0] == key:
                self.array[index] = (key, data)
                return
            else:
                index = (index + 1) % self.table_size
        raise Exception("hash table is full")

    def __getitem__(self, key):
        index = self.hash_function(key)

        for _ in range(self.table_size):
            if self.array[index] is None:
                raise Exception("key not exist")
            elif self.array[index][0] == key:
                return self.array[index][1]
            else:
                index = (index + 1) % self.table_size
        raise Exception("key not found")


HT = HashTableLinear()
HT["FIT1008"] = "Intro to CS"
HT["FIT2004"] = "ADS"
# HT.insert("FIT1008", "Intro to CS")
# HT.insert("FIT2004", "ADS")

print(len(HT))
print(HT["FIT2004"])







