class MaxHeap(object):
    def __init__(self, array):
        self.heapList = array 
        self.heapSize = len(array) 
    
    def __str__(self):
        return str(self.heapList)
    
    def get_left(self, index):
        return (index * 2) + 1

    def get_right(self, index):
        return (index * 2) + 2

    def get_parent(self, index):
        return (index - 1)/2

    def get_max(self):
        self.heapList[0] 
    
    # conform to heap properties
    # left and right subtrees of index must already conform
    # https://www.baeldung.com/cs/binary-tree-max-heapify
    def max_heapify(self, index=0):
        leftIndex = self.get_left_child(index) # get left child index
        rightIndex = self.get_right_child(index) # get right child index
        greatestIndex = index #setting it to index initially

        # if left index is out of bounds, don't call for it's value!
        # if the left child is greater, assign it to greatestIndex 
        if leftIndex < self.heapSize and self.heapList[leftIndex] > self.heapList[greatestIndex]:
            greatestIndex = leftIndex
        
        # same with right
        if rightIndex < self.heapSize and self.heapList[rightIndex] > self.heapList[greatestIndex]:
            greatestIndex = rightIndex
        
        # if the index is not the greatest value, swap it so that it is
        if greatestIndex != index:
            greatest = self.heapList[greatestIndex] #this var is just for swapping purposes
            self.heapList[greatestIndex] = self.heapList[index]
            self.heapList[index] = greatest # do the swap
            self.max_heapify(greatestIndex) # keep working up the tree?

    # enforces the properties of a max heap
    # starts at end of array and loops backwards
    def build_max_heap(self):
        # leaf nodes already conform to max heap properties,
        # so this index value will give us the index minus the leaves
        index = (self.heapSize / 2) - 1
        while index >= 0:
            # call max_heapify on the index (both children are max heaps)
            self.max_heapify(index)
            index = index - 1 # then loop backwards
    
    # remove max value from heap and reassert heap rules
    def extract_max(self):
        maxValue = self.heapList # get max value
        lastIndex = self.heapSize - 1 # get index of last element
        self.heapList[0] = self.heapList[lastIndex] #assign last value to position 0 in array
        self.heapSize = self.heapSize - 1 # reduce heap size
        del(self.heapList[lastIndex]) # delete copied leaf node
        self.max_heapify(0) # now ensure heap conforms to max heap properties
        return maxValue 

    # increase key at index to new value and then assert heap rules
    def increase_key(self, index, value):
        self.heapList[index] = value # assign new value to index position
        child = self.heapList[index] # now assign it to var child
        parent = self.heapList[self.get_parent(index)] # get child's parent
        if child >= parent: # if child is greater than parent, switch values
            self.heapList[self.get_parent(index)] = child
            self.heapList[index] = parent
        self.build_max_heap() # then assert heap properties

    # use increase_key to move key to 0 position, then call extract_max
    def delete_key(self, index):
        self.increase_key(index, float('+inf'))
        self.extract_max()

    # add new node at end of tree and assert heap properties
    def insert(self, value):
        index = self.heapSize # get last index
        self.heapList.append(value) # add new node at end
        self.heapSize += 1 # increase size value
        self.increase_key(index, value) # this will assert heap properties


