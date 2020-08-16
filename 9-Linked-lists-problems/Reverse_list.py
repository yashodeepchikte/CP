# reverse the list inplece in constant time complexity
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def reverse_list(head):
    # check if the list has any cycles if it does then break the code 
    slow = head
    fast = head
    while True:
        if slow.next == None or fast.next == None or fast.next.next == None:
            break
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print("The list has a cycle so it cannot be reversed")
            return None
    temp = head
    prev = None
    while temp:
        actual_next = temp.next
        temp.next = prev
        prev = temp
        temp = actual_next
    return prev




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
f.next = None


new_head = reverse_list(head)
temp = new_head
while temp:
    print(temp.value)
    temp =temp.next

# if the list contains a cycle the  list that will be printed   