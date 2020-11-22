

# Each node is a binary tree in itself thus all 
# all the methods that we can call on a tree we can also call on a branch or leaf

class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.rightChild = None
        self.leftChild = None
    def insertLeft(self, value):
        t = BinaryTree(value)
        t.leftChild = self.leftChild
        self.leftChild = t
    def insertRight(self, value):
        t = BinaryTree(value)
        t.rightChild = self.rightChild
        self.rightChild = t

Root = BinaryTree(10)
Root.insertLeft(20)
Root.insertLeft(30)
Root.insertRight(200)

# inserting  a node at another level
Root.leftChild.insertRight(3000)