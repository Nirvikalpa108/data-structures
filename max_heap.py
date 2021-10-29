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
    
    # mutates the heapList to ensure conforms to max heap properties
    # a condition of this function is that the left and right subtrees of index already conform
    # https://www.baeldung.com/cs/binary-tree-max-heapify
    def max_heapify(self, index=0):
        pass

    # enforces the properties of a max heap
    def build_max_heap(self):
        pass
    
    # remove min value from heap and reassert heap rules
    def extract_max(self):
        pass

    # ** is this right??? It's decrease key for min heap, is it increase key for max heap???    
    # increase key at index to new value and then assert heap rules
    def increase_key(self, index, value):
        pass

    def delete_key(self, index):
        pass

    def insert(self, value):
        pass


