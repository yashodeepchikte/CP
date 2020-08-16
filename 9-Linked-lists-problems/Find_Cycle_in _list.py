# This function takes in the head of the linked list and returns a boolean indicating weather the list has a cycle in it or not

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def check_for_cycle(head):
    if head.next == None:
        print("The list has only one node --> No cycle")
        return 0
    slow = head
    fast = head.next
    while True:
        if slow == fast:
            return 1
        if fast == None or slow == None:
            return 0

        fast = fast.next.next
        slow = slow.next



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

check_for_cycle(head)
