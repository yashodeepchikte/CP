class Node:
    def __init__(self, value, priority):
        self.priority = priority
        self.value = value

# Min Priority Queue
class PriorityQueue:
    def __init__(self):
        self.values = []

    def enqueue(self, value, priority, show = False):
        # inserts the value as per the priority in the PQ
        node = Node(value, priority)
        if len(self.values) == 0:
            self.values.append(node)
            return
        self.values.append(node)
        child_index = len(self.values)-1
        
        while True:
            parent_index = int((child_index-1)//2)
            if parent_index < 0:
                break
            parent = self.values[parent_index]
            child = self.values[child_index]
            
            if child.priority < parent.priority:
                self.values[parent_index] = child
                self.values[child_index] = parent
                child_index = parent_index
            else:
                break
        if(show):
            self.show_PQ()
    def dequeue(self):
        # Removes and returns the lowest priority Element
        if len(self.values) == 0:
            print("Priority Queue is already empty")
            return 
        if len(self.values) == 1:
            return self.values.pop()
        self.values[0], self.values[len(self.values)-1] = self.values[len(self.values)-1], self.values[0]
        min_priority_element = self.values.pop()
        parent_index = 0
        
        while True:
            if(parent_index > len(self.values)-1):
                print("Debug --> brealing because parent_index > len(self.values)-1")
                break
            parent = self.values[parent_index]
            
            child1_index = 2*parent_index + 1
            if child1_index > len(self.values) - 1:
                print("Debug --> brealing because child1_index > len(self.values) - 1")
                break
            child1 = self.values[child1_index]
            child2_index = parent_index * 2 + 2
            if child2_index > len(self.values) - 1:
                child2_index = child1_index
            child2 = self.values[child2_index]
            
            if child1.priority < parent.priority or child2.priority < parent.priority:
                if child1.priority <= child2.priority:
                    self.values[parent_index] = child1
                    self.values[child1_index] = parent
                    parent_index = child1_index
                else:
                    self.values[parent_index] = child2
                    self.values[child2_index] = parent
                    parnet_index = child2_index
            else:
                break
        return min_priority_element
        
        
        
    def show_PQ(self):
        # Prints the elements of the PQ along with their children
        PQ = self
        for i, j in enumerate(PQ.values):
            print("-----------------------------------------------------")
            print("Value = ", j.value, " priority = ", j.priority)
        #     print(" i =", i, " j = ", j)
            child1_index = i * 2 + 1
            child2_index = i * 2 + 2
            if child1_index < len(PQ.values) - 1:
                print("Child1-priority = ", PQ.values[child1_index].priority)
            if child2_index < len(PQ.values) - 1:
                print("Child2-Priority = ", PQ.values[child2_index].priority)
            print("  ")
        print("Priorities in order ---> ", end = " ")
        for i in PQ.values:
            print(i.priority, end = " ")


# Insertion ---> O(log(n))
# Removal ------> O(log(n))
# searching ----> O(lor(n))