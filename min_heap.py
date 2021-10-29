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
    
    # remove min value from heap and reassert heap rules
    def extract_min(self):
        minValue = self.heapList[0] 
        lastIndex = self.heapSize - 1
        # assigning last value to position 0
        self.heapList[0] = self.heapList[lastIndex]
        # reduce heap size 
        self.heapSize = self.heapSize - 1
        # delete copied leaf element 
        del(self.heapList[lastIndex])
        # now sort out the heap (the children already conform)
        self.min_heapify(0)
        return minValue
    
    # decrease key at index to new value and then assert heap rules
    def decrease_key(self, index, value):
        self.heapList[index] = value
        child = self.heapList[index]
        parent = self.heapList[self.get_parent(index)]  
        # if the new value is less than or equal to the parent,
        if child <= parent:
            # switch the values
            self.heapList[self.get_parent(index)] = child
            self.heapList[index] = parent  
        # then assert heap properties
        self.build_min_heap()  

    # Add a new node at the end of the tree. 
    # use decrease_key function to decrease to the value you want
    # the decrease_key function will deal with moving to where it needs to be
    def insert(self, value):
        # get the last index
        index = self.heapSize 
        # add new node 
        self.heapList.append(value) 
        self.heapSize += 1
        self.decrease_key(index, value)

    # use decrease_key function to move the key to 0 with negative_infinity = float('-inf')
    # then call extract_min
    def delete_key(self, index):
        self.decrease_key(index, float('-inf'))
        self.extract_min()
    
    # enforces the properties of a min heap
    def build_min_heap(self):
        # loop starting at end array, working backwards
        # skip the leaf nodes as they already conform to min_heapify conditions
        index = (self.heapSize / 2) -1
        while index >= 0: 
            # call min_heapify on index 0 (by that point, both children are min heaps)
            self.min_heapify(index)
            index = index - 1
    
    # h/w complete max heap
    # h/w write heap sort algorithm
    # look at heap sort if time - efficient sorting algorithm
    # repeatedly calling extract min and putting the result into an array

myHeap = MinHeap([4,1,7,2,9,3,5,17,6,11])
print(myHeap)
myHeap.build_min_heap()
print(myHeap)
print(myHeap.extract_min())
print(myHeap)
myHeap.decrease_key(1, 1)
print(myHeap)
myHeap.insert(20)
print(myHeap)



