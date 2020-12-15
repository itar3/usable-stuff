class TreeNode:

    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

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









