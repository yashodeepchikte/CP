class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.previous = None
        
class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 
    def treverse(self):
        # print the linked list
        temp = self.head
        index = 0
        while temp:
            if index == 0:
                print("\n----------------------HEAD-----------------------")
                if(temp.next):
                    print("index = ", index, " value = ", temp.val ," next = ", temp.next.val, " previous = Null")
                else:
                    print("index = ", index, " value = ", temp.val ," next = Null", " previous = Null")
            elif index == self.length -1:
                print("\n----------------------TAIL-----------------------")            
                print("index = ", index, " value = ", temp.val ," next = Null", " previous = ", temp.previous.val)
            else:
                print("\n-------------------------------------------------") 
                print("index = ", index, " value = ", temp.val ," next = ", temp.next.val, " previous = ", temp.previous.val)
            temp = temp.next
            index += 1
        print("\nLength = ", self.length)
    def push(self, value):
        # adds a node at the end
        node = Node(value)
        if self.length == 0 :
            self.head = node
            self.tail = node
            self.head.next = self.tail
            self.tail.previous = self.head
            self.length = 1
            return self
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
            self.length += 1
            return self
    def pop(self):
        if self.length == 0:
            print("linked list already empty")
            return None
        elif self.length == 1:
            temp = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        elif self.length > 1:
            temp = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            self.length -= 1 
            return temp
    def shift(self):
        # removing the first node in a LL
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        elif self.length > 1:
            temp = self.head
            self.head = self.head.next
            self.head.previous = None
            self.length -= 1
            return temp
    def unshift(self, value):
        # Adding a node to the Starting
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
            self.head.next = self.tail
            self.tail.previous = self.head
            self.length = 1
            return None
        elif self.length > 1:
            temp = self.head
            self.head.previous = node
            self.head = node
            self.head.next = temp 
            self.length += 1
            return self 
    def get(self, index):
        # get the value at the mentioned index
        if(self.length == 0):
            print("Linked List is empty")
            return
        elif(index > self.length-1 or index < 0):
            print("index out of range")
            return
        else:
            if index < self.length - index:
                # move from start to end
                temp = self.head
                for i in range(index):
                    temp = temp.next
                return temp.val
            else:
                # move from end to the start
                temp = self.tail
                for i in range(self.length - index-1):
                    temp = temp.previous
                return temp.val
    def get_node(self, index):
        # get the node at the mentioned index
        if(self.length == 0):
            print("Linked List is empty")
            return
        elif(index > self.length-1 or index < 0):
            print("index out of range")
            return
        else:
            if index < self.length - index:
                # move from start to end
                temp = self.head
                for i in range(index):
                    temp = temp.next
                return temp
            else:
                # move from end to the start
                temp = self.tail
                for i in range(self.length - index-1):
                    temp = temp.previous
                return temp
    def set(self, index, value):
        # set the value of node at the mentioned index to the given value
        temp = self.get_node(index)
        if temp:
            temp.val = value
            return True
        else:
            print("index out of range")
            return False
    def insert(self, index, value):
        node = Node(value)
        # create a node with the given value and inset it to the given index
        if(index > self.length or index < 0):
            print("index out of range")
            return False
        elif index == 0:
            self.unshift(value)
            return True
        elif index == self.length:
            self.push(value)
            return True
        else:           
            temp = self.get_node(index-1)
            ahead = self.get_node(index)
            temp.next = node
            node.previous = temp 
            node.next = ahead
            ahead.previous = node
            self.length += 1
            return True
            
    def remove(self, index):
        if self.length == 0:
            print("Linked list is already empty")
            return None
        if index > self.length -1 or index < 0:
            print("index is out of range")
            return None
        elif index == 0:
            return self.shift()
        elif index == self.length -1:
            return self.pop()
        else:
            prev = self.get_node(index-1)
            current = self.get_node(index)
            ahead = self.get_node(index+1)
            prev.next = ahead
            ahead.previous = prev
            self.length -= 1
            return current
# Big O analysis
# Insertion   - O(1)
# Removal     - O(1)
# Searching   - O(N) technically O(N/2)
# Access      - O(N) technically O(N/2)