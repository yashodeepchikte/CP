class Node:
    def __init__(self,val=None, next=None):
        self.val = val
        self.next = next
        
class SinglyLinkedList :
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def push(self, value):
        if(self.head != None):
            node = Node(value)
            self.tail.next = node
            self.tail = node
            self.length += 1
        else:
            node = Node(value)
            self.head = node
            self.tail = node
            self.length = 1
        return self
    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        elif self.length > 1:
            temp = self.head.next
            pre = self.head
            while True:
                pre = pre.next
                temp = temp.next   
                if temp == self.tail or temp.next == None:
                    break
            
            self.tail = pre
            self.tail.next = None
            self.length -= 1

            return temp.val  
    def shift(self):
        # Removes the node from the begning
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return None
        elif self.length > 1:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            return temp.val
    def unShift(self, val):
        # adding a node to the start
        if self.length == 0:
            self.head = Node(val)
            self.tail = self.head
            self.length += 1
        else:
            temp = self.head
            self.head = Node(val)
            self.head.next = temp
            self.length += 1
    def get(self, index):
        # returns the value at the given index
        if index > self.length -1 or index < 0:
            print("Given index to the get method out of linked link's lenth")
            return None
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp.val
    def get_node(self, index):
        # return the node at the given index
        if index > self.length -1 or index < 0:
            print("Given index to the get_node method out of linked link's lenth")
            return None
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp
        
    def set(self, index, value):
        # set the value of the node at the mentioned index to the given value
        temp = self.get_node(index)
        if temp:
            temp.val = value
            return temp.val
        else:
            print("the index passed to the set Method is outside the lendth of the linked list")
    def insert(self, index, value):
        # takes the value creates a new node and inserts it at the given index
        node = Node(value)
        if index > self.length or index < 0:
            print("Index out of range")
            return False
        elif index == 0:
            temp =self.head
            self.head = node
            self.head.next = temp
            self.length += 1 
            return True
        elif index == self.length:
            temp = self.tail
            self.tail.next = node
            self.tail = node
            self.length += 1
            return True
        else:
            temp = self.get_node(index)
            pre = self.get_node(index-1)
            if temp and pre:
                pre.next = node
                node.next = temp
                self.length += 1
                return True
            else:
                print("inde out of range")
                return True
    def remove(self, index):
        # removes node from the given index
        if self.length == 0:
            print("Linked list is already empty")
            return None
        elif index < 0 or index > self.length-1:
            print("Index out of bounds")
            return None
       
        else:
            if index == 0:
                return self.shift()
            elif index == self.length - 1:
                return self.pop()
            else:
                pre = self.get_node(index-1)
                post= self.get_node(index+1)
                pre.next = post
                self.length -= 1 
    def reverse(self):
        # reverse the linked list inplace - do not create a copy
        if self.length <= 1:
            print("Linled list is empty")
            return
        start = self.head
        end = self.tail
        
        current = start
        previous = None
        ahead = current.next
        
        while current != self.tail:
            actual_next = current.next
            current.next = previous
            previous = current
            current = actual_next
        self.tail.next = previous
        self.head = end
        self.tail = start
        self.tail.next = None
            
            
    def treverse(self):
        print("this is the linked list -->")
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
        print("Length = ", self.length)
        
        
# Big O analysis
# Push = O(1)
# Pop  = O(1)
# Shift/UnShift = O(1)
# Insertion = O(1) -- strictly speaking we will have to traverse till the previous and next node to insert but actual insertion is O(1)
# Access = O(N)
# removal = best O(1) to worst O(n) 
# searching = best O(1) to worst O(n)
# Reversal = O(n)



linkedList = SinglyLinkedList()
linkedList.push(1)
linkedList.push(2)
linkedList.push(3)
linkedList.push(4)
