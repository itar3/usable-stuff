class Node:
    def __init__(self,item,next):
        self.item = item
        self.next = next

class List:
    def __init__(self):
        self.head = None
        self.count = 0

    def getNode(self,index):
        node = self.head
        if index == 0:
            return node
        else:
            for i in range(index):
                node = node.next
        return node


    def insert(self,item,index):

        if index == 0:
            self.head = Node(item,self.head)
        else:
            node = self.getNode(index - 1)
            node.next = Node(item, node.next)
        self.count+=1

    def delete(self, index):

        if index == 0:
            item = self.head.item
            self.head = self.head.next
        else:
            node = self.getNode(index - 1)
            item = node.next.item
            node.next = node.next.next

        self.count-=1
        return item

