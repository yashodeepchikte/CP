class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.length = 0
        self.depth = 0

class BinarySearchTree:
    
    def __init__(self, root = None):
        self.depth = 0
        self.length = 0
        if root != None:
            self.root = Node(root)
            self.length = 0
        else:
            self.root = root
            self.length = 1
            self.depth = 1
    
    def insert(self, value):
        # Insert a value into the binary tree
        node = Node(value)
    
        if self.root == None:
            self.root = node
            self.length = 1
            self.depth = 1
            print("depth = 1")
            return
        elif self.root:
            temp = self.root
            depth_count = 1
            print("for inserting ", value, " --->", end=" ")
            while True:
                depth_count += 1
                if value > temp.value:
                    print("Right", end = " ")
                    if temp.right:
                        temp = temp.right
                        continue
                    else:
                        temp.right = node
                        break
                else:
                    print("Left", end = " ")
                    if temp.left:
                        temp = temp.left
                        continue
                    else:
                        temp.left = node
                        break
            print("Depth = ", self.depth)
            print("Number of nodes = ", self.length)
            print(" ")
        
            if(depth_count > self.depth):
                self.depth = depth_count
            self.length += 1
            return self
    def check(self, value):
        # check if the given value is present in the tree
        if self.root == None:
            print(" the binary search tree is empty")
            return False
        if value == self.root.value:
            return True
        else:
            temp = self.root
            while True:
                if temp == None:
                    print("value ", value, " not found in the Binary Search Tree")
                    return False
                if value == temp.value:
                    return True
                if value > temp.value:
                    temp = temp.right
                else:
                    temp = temp.left
            return False
    def BFS(self):
         #     10
         #   6     15
         # 3   8      20
         # ---> [10, 6, 15, 3, 8, 20]

        if self.root == None:
            return []
        else:
            queue = []
            visited = []
            
            queue.append(self.root)
            
            while len(queue) > 0:
                current = queue[0]
                queue = queue[1:]
                visited.append(current.value)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            return visited
    def DFS_PreOrder(self):
        
        #     10
        #   6     15
        # 3   8      20
        # ---> [10, 6, 3, 8, 15, 20]
          
        
        data = []
        current = self.root
        
        def treverse(node):
            data.append(node.value)
            if node.left:
                treverse(node.left)
            if node.right:
                treverse(node.right)
        treverse(current)
        
        return data
                
    def DFS_PostOrder(self):
            #     10
            #   6     15
            # 3   8      20
            # ---> [3, 8, 6, 20, 15, 10]
            # we visit a node after we have vidited all of its left and then all the right children
        data = []
        current = self.root
        
        def treverse(node):
            if node.left:
                treverse(node.left)
            if node.right:
                treverse(node.right)
            data.append(node.value)
        treverse(current)
        
        return data
    def DFS_InOrder(self):
        # treverse entire left nodes and then visit the node then its right side
        #     10
        #   6     15
        # 3   8      20
        # ---> [3, 6, 8, 10, 15, 20]
        # we visit a node after we have vidited all of its left and then all the right children
        data = []
        current = self.root
        
        def treverse(node):
            if node.left:
                treverse(node.left)
            data.append(node.value)
            if node.right:
                treverse(node.right)
            
        treverse(current)
        
        return data
                
# Big O analysis
# insertion ---> ordinary case O(Log(n)) worst case O(n) if the BTS is skewed height = n
# Searching ---> ordinary case O(Log(n)) wordt case O(n) if the BTS is skewed height = n 