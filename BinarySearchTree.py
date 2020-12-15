class BSTNode:
    def __init__(self, key=None, item=None, left=None, right=None):
        self.key = key
        self.item = item
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def __setitem__(self, key, data):
        self.root = self.setitem_aux(self.root, key, data)

    def setitem_aux(self, current, key, data):
        if current is None:
            current = BSTNode(key, data)
        elif key < current.key:
            current.left = self.setitem_aux(current.left, key, data)
        elif key > current.key:
            current.right = self.setitem_aux(current.right, key, data)
        else:
            current.item = data
        return current

    def __getitem__(self, key):
        return self.getitem_aux(self.root, key)

    def getitem_aux(self, current, key):
        if current is None:
            raise Exception("key not found")
        elif key == current.key:
            return current.item
        elif key < current.key:
            return self.getitem_aux(current.left, key)
        else:
            return self.getitem_aux(current.right, key)

    def print_preorder(self):
        self.preorder_aux(self.root)

    def preorder_aux(self, current):
        if current is not None:
            print(current.item)
            self.preorder_aux(current.left)
            self.preorder_aux(current.right)


BST = BinarySearchTree()
BST[1008] = "Intro to CS"
BST[500] = "DS"
BST[2004] = "ADS"
BST[1500] = "OS"
BST[100] = "C++"

BST.print_preorder()
print(BST[2004])











