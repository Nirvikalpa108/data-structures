# Properties of Heaps
# https://medium.com/swlh/data-structures-heaps-b039868a521b 
# Heaps are not sorted. There is no particular relationship between nodes at any level.
# They are usually implemented using arrays, which save overhead cost of storing pointers to child nodes.
# disadvantage of heaps - only provide O(1) access to the smallest/greatest item. Finding other items in the heap takes O(n) time.
# In complete binary trees, each level is filled up before another level is added and the levels are filled from left to right.
# Insert, delete are O(log(n))

# Consider learning about the inbuilt heap functions that python offers:
# from heapq import heappush, heappop, heapify 
# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining heap invarient
# heapify - transform list into heap, in place, in linear time


class MinHeap(object):
    def __init__(self, array):
        self.heapList = array # consider changing this.
        self.heapSize = len(array) # come back to this too.
    
    def __str__(self):
        return str(self.heapList)
    
    def insert(self, value):
        return self.heapList.append(value)
    
    def get_left(self, index):
        return (index * 2) + 1

    def get_right(self, index):
        return (index * 2) + 2

    def get_parent(self, index):
        return (index - 1)/2

    def get_min(self):
        self.heapList[0] 

    # mutates the heapList to ensure conforms minHeap properties
    # a condition of this function is that the left and right subtrees of index are already minHeaps
    # https://www.baeldung.com/cs/binary-tree-max-heapify
    def min_heapify(self, index=0):
        leftIndex = self.get_left(index)
        rightIndex = self.get_right(index)
        smallestIndex = index #setting it to index initially, will change if required

        # if left index is out of bounds, don't call for it's value!
        if leftIndex < self.heapSize and self.heapList[leftIndex] < self.heapList[smallestIndex]:
            smallestIndex = leftIndex
        
        # same with right
        if rightIndex < self.heapSize and self.heapList[rightIndex] < self.heapList[smallestIndex]:
            smallestIndex = rightIndex

        if smallestIndex != index:
            # swap
            smallest = self.heapList[smallestIndex] #often named temp (just for swapping purposes)
            self.heapList[smallestIndex] = self.heapList[index]
            self.heapList[index] = smallest
            self.min_heapify(smallestIndex)
    
    # remove head and call min_heapify to re-order heap
    def extract_min(self):
        pass
    
    # *** I don't understand this one
    # decrease key at index to new value 
    # assumes that this is smaller than the existing value
    def decrease_key(self, index, value):
        pass

    # delete key at index
    # first reduce value to minus infinite 
    # negative_infinity = float('-inf')
    # then call extract_min 
    def delete_key(self, index):
        pass

myHeap = MinHeap([4,1,7,2,9])
print(myHeap)
myHeap.min_heapify()
print(myHeap)
myHeap.insert(3)
print(myHeap)
myHeap.min_heapify() # this doesnt seem to be working
print(myHeap)




