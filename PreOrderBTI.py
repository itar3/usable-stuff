class TreeNode:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class PreOrderBTIterator:
    def __init__(self, root):
        self.current = root
        self.stack = []
        self.stack.append(root)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration
        current = self.stack.pop()
        if current.right is not None:
            self.stack.append(current.right)
        if current.left is not None:
            self.stack.append(current.left)
        return current.item


class BinaryTree:
    def __init__(self):
        self.root = None

    def __iter__(self):
        return PreOrderBTIterator(self.root)

    def __len__(self):
        return self.len_aux(self.root)

    def len_aux(self, current):
        if current is None:
            return 0
        else:
            return 1 + self.len_aux(current.left) + self.len_aux(current.right)

    def get_leaves(self):
        alist = []
        self.get_leaves_aux(self.root, alist)
        return alist

    def get_leaves_aux(self, current, alist):
        if current is not None:
            if self.is_leaf(current):
                alist.append(current.item)
            else:
                self.get_leaves_aux(current.left, alist)
                self.get_leaves_aux(current.right, alist)

    def is_leaf(self, current):
        return current.left is None and current.right is None

    def is_empty(self):
        return self.root is None

    def add(self, item, pos_bitstring):
        bitstring_iterator = iter(pos_bitstring)
        self.root = self.add_aux(self.root, item, bitstring_iterator)

    def add_aux(self, current, item, bitstring_iterator):
        if current is None:
            current = TreeNode()

        try:
            bit = next(bitstring_iterator)
            if bit == "0":
                current.left = self.add_aux(current.left, item, bitstring_iterator)
            elif bit == "1":
                current.right = self.add_aux(current.right, item, bitstring_iterator)
        except StopIteration:
            current.item = item
        return current

    def print_preorder(self):
        self.preorder_aux(self.root)

    def preorder_aux(self, current):
        if current is not None:
            print(current.item)
            self.preorder_aux(current.left)
            self.preorder_aux(current.right)


BT = BinaryTree()
BT.add(3, "")
BT.add(5, "0")
BT.add(1, "1")
BT.add(6, "01")
BT.print_preorder()
print()

for item in BT:
    print(item)

print(len(BT))
print(BT.get_leaves())









