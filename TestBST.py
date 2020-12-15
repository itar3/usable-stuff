class BSTnode:
    def __init__(self, key = None, item = None, left = None, right = None):
        self.key = key
        self.item = item
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def getMax(self):
        if self.is_empty():
            raise Exception("BST is empty")
        if self.root.right == None:
            item  = self.root.item
            self.root = self.root.left
            return item
        else:
            self.get_max_aux(self.root, self.root.right)

    def get_max_aux(self, parent, current ):
        if self.current.right == None:
            item = current.item
            current = current.left
            return item
        else:
            self.get_max_aux(self, current, current.right)

    def insert(self, key, data):
        self.root = self.insert.aux(self, self.root, key, data)

    def insert_aux(self, current, key, data):
        if current == None:
            current = BSTnode(key, data)
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, data)
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, data)
        else:
            current.item = data


    def get_item(self, key):
        return self.get_item_aux(self.root, key)

    def get_item_aux(self, current, key):
        if current == None:
            raise Exception("key not found")
        elif key == current.key:
            return current.item
        elif key < current.key
            return self.get_item_aux(current.left, key)
        elif key > current.key:
            return self.get_item_aux(current.right, key)


        def print_preorder(self):
            return self.print_preorder_aux(self.root)

        def print_preorder_aux(self, current):
            print(current)
            self.print_preorder_aux(current.left)
            self.print_preorder_aux(current.right)

        def sum_leaves(self):
            return self.sum_leaves_aux(self.root)
        def sum_leaves_aux(self, current):
            if current == None:
                return 0
            elif current.left == None and current.right == None:
                return current.item
            else:
                left = self.sum_leaves_aux(current.left)
                right = self.sum_leaves_aux(current.right)
                return left+right


        def __len__(self):
            return self.len_aux(self.root)
        def len_aux(self,current):
            if current == None:
                return 0
            else:
                leftLen = len_aux(current.left)
                rightLen = len_aux(current.right)
                return 1+ max(leftLen, rightLen)

        def getMax(self):
            if self.root == None:
                raise Exception("BST is empty")
            elif self.root.right == None:
                item = self.root.item
                self.root = self.root.left
                return item
            else:
                return getMax_aux(self.root,self.root.right)


        def getMax_aux(self, parent, current):
            if current.right == None:
                item = current.item
                parent.right = current.left
                return item
            else:
                return getMax_aux(current, current.right)


        def insert(self, key, item):
            self.root = self.aux_insert(self.root, key, item)
        def aux_insert(self, current, key, item):
            if current == None:
                current = BSTnode(key,item)
            if key < current.key:
                current.left = aux_insert(current.left, key,item)
            if key > current.key:
                current.right = aux_insert(current.right, key, item)
            else:
                current.item = item
            return current


        def find(self, key):
            return self.find_aux(self.root, key)
        def find_aux(self, current, key):
            if current == None:
                raise Exception("key not found")
            elif key < current.key:
                return self.find_aux(current.left, key)
            elif key > current.key:
                return self.find_aux(current.right,key)
            elif key == current.key:
                return current.item


