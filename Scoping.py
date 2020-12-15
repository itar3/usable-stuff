class myclass:
    def __init__(self,x):
        self.x = x
    def a(self):
        self.x = self.x + 1
    def b(self):
        self.x = x + 2
    def c(self):
        x = self.x + 3
    def __str__(self):
        return str(self.x)
    def a(x):
        x=x-1
    def b():
        x=x+2

x=7
myobject = myclass(x)
myobject.c()
print(x)


def self.k_largest(self, k):
    list = []
    self.k_aux(self.root,k, list)
    return list[-1]

def self.k_aux(self, current, k, list):
    if current !=0:
        ans = self.k_aux(current.right, k, list)
        if ans != 0:
            return ans
        list.append(current.key)
        if len(list) == k:
            return list
        ans = self.k_aux(current.left,k,list)
        if ans != 0:
            retrun ans

def getMax(self):
    if self.root.right == None:
        item = self.root.item
        self.root = self.root.left
        return item
    else:
        return self.getmaxaux(self.root, self.root.right)

def getmaxaux(self, parent, current):
    if current.right == None:
        item = current.item
        parent.right = current.left
        return item
    else:
        return self.getmaxaux(current, current.right)


def len(self):
    return self.lenaux(self.root)
def self.lenaux(self, current)
    if current == None:
        return 0
    else:
        leftLen = self.lenaux(current.left)
        rightLen = self.lenaux(current.right)
        return 1+ max(leftLen,rightLen)


def sum_leaves(self):
    return sum_leaves_aux(self.root)
def sum_leaves_aux(self, current):
    if current == None:
        return 0
    elif current.right == None and current.left == None
        return current.item
    else:
        left = sum_leaves_aux(current.left)
        right = sum_leaves_aux(current.right)
        return right + left

def range(self, a ,b):
    list = []
    self.range_aux(self.root, a ,b, list)
    return list

def range_aux(current, a ,b, list):
    if current == None
        return
    elif a<current.key:
        self.range_aux(current.left, a ,b, list)
    elif a<=current.key<=b:
        list.append(current.key)
    elif b> current.key:
        self.range_aux(current.right, a ,b , list)
