# given a head and n find the nth node from the end
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# we start with 2 pointers
# initially both are at the head
# then we move right pointer n steps ahead
# then we start moving both the pointer by one step until right one reaches the end
# when right reaches the end it was n nodes ahed of the left node thus the left node is the nth from end

def nth_last_node(head, n):
    left_ponter = head
    right_pointer = head
    for i in range(n):
        if right_pointer == None:
            print("value of n is larger than the length of the list")
            return None
        right_pointer = right_pointer.next
    
    while right_pointer:
        right_pointer = right_pointer.next
        left_ponter = left_ponter.next
    
    return left_ponter


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
f.next = None

nth_last_node(head, 3)