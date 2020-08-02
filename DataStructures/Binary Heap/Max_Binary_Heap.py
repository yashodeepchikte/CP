# Max Heap
class MaxBinaryHeap:
    def __init__(self):
        self.values = []
        
    def insert(self, value):
        self.values.append(value)
        index = len(self.values)-1
        while True:
            parent_index = (index-1)//2
            parent = self.values[parent_index]
            if value <= parent or parent_index < 0:
                break
            self.values[parent_index] = value
            self.values[index] = parent
            index = parent_index
        return self.values
    
    def extractMax(self):
        self.values[0], self.values[-1] = self.values[-1], self.values[0]
        if len(self.values) < 1:
            return self.values[0]
        max_val = self.values.pop()
        parent_index = 0
        while True:
            child1_index = parent_index*2 + 1
            child2_index = parent_index*2 + 2
            if parent_index > len(self.values) -1:
                break
            parent_value = self.values[parent_index]
            if child1_index > len(self.values)-1:
                # we have reached the leaf
                break
            if child2_index > len(self.values)-1 and child1_index <= len(self.values)-1:
                # no right child ie we are at the terminal and only one leaf is present
                child2_index = child1_index
            
            child1 = self.values[child1_index]
            child2 = self.values[child2_index]
            if child1 > parent_value or child2 > parent_value:
                if child1 < child2:
                    self.values[child2_index] = parent_value
                    self.values[parent_index] = child2
                    parent_index = child2_index
                else:
                    self.values[child1_index] = parent_value
                    self.values[parent_index] = child1
                    parent_index = child1_index
            else:
                break
        return max_val
                