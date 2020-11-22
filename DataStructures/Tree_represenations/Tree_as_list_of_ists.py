
# We store the value of the root node as the first element
# the second element of the list will be a list in itself that represents the left chilf of the root the third will repersent the right child
# continue nesting each list accordingly is no children leave the list empty

def binary_tree(root):
	return [root , [], []]

def insert_left(root, branch):
	t = root.pop(1)
	root.insert(1, [branch, t, []])
	return root

def insert_right(root, branch):
	t = root.pop(2)
	root.insert(2, [branch, [], t])
	return root

def get_root(root):
	return root[0]

def get_left_child(root):
	return root[1]

def get_right_child(root):
	return root[2]




r = binary_tree(10)
insert_left(r, 20)
insert_right(r, 30)
