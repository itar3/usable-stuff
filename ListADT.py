class MyList:
    def __init__(self, size):
        self.count = 0
        # self.array = build_array(size)
        self.array = [0] * size

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count >= len(self.array)

    def add(self, item):
        still_has_space = not self.is_full()
        if (still_has_space):
            self.array[self.count] = item
            self.count += 1
        return still_has_space

    def delete(self, index):
        valid_index = index >= 0 and index < self.count

        if valid_index:
            for i in range(index, self.count - 1):
                self.array[i] = self.array[i + 1]
            self.count -= 1
        return valid_index

    def print_all(self):
        for i in range(self.count):
            print(self.array[i])

    def __str__(self):
        ret = ""
        for i in range(self.count):
            ret = ret + str(self.array[i]) + ","
        return ret

    def __len__(self):
        return self.count

    def __contains__(self, item):
        for i in range(self.count):
            if self.array[i] == item:
                return True
        return False


mylist = MyList(6)
print(mylist.add(2))
print(mylist.add(3))
print(mylist.add(4))
print(mylist.add(5))
print(mylist.delete(2))
print(str(mylist))
mylist.print_all()
print(len(mylist))

print(8 in mylist)

# mylist[2] =3
