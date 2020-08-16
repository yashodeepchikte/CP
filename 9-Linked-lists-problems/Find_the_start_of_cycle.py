# This function takes in the head of the linked list and returns a node (value at that node) indicating where the cycle started return -1 if no cycle
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

from time import sleep 
def find_cycle_start(head):
    if head.next == None:
        print("List has only one node ------> thus no cucles")
        return -1
    slow = head
    fast = head
    
    while True:
        if slow == None or fast == None:
            return -1
        
        slow = slow.next
        
        fast = fast.next.next
        if slow == fast:
            break
            
        
        
    if slow != fast:
        return -1
    slow = head
    while slow != fast:
        print(" ----------------------------------------------------------- ")
        print("slow = ", slow.value)
        print("fast = ", fast.value)
        sleep(1)
        slow = slow.next
        fast = fast.next
    print(" ----------------------------------------------------------- ")
    print("slow = ", slow.value)
    print("fast = ", fast.value)
    return slow


# Starter code
head = Node(0)
a = Node(20)
b = Node(30)
c = Node(40)
d = Node(50)
e = Node(60)
f = Node(70)
head.next = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = c

find_cycle_start(head)