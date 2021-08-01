# https://docs.python.org/3/library/ctypes.html 
import ctypes

# AP double check delete operation
# consider increasing default capacity so resizing operation doesnt happen so often

class DynamicArray(object):
    # create a new array
    def __init__(self): # __init__() is executed when an instance is created. self refers to the instance that is being created.
        self.index = 0 # count elements (default is 0)
        self.capacity = 1 # default capacity 
        self.array = self.make_array(self.capacity)    
    
    # returns length    
    def __len__(self):
        return self.index
    
    # return element at index k 
    def __getitem__(self,k):
        if not 0 <= k <self.index:
            return IndexError('K is out of bounds!') # Check it k index is in bounds of array       
        return self.array[k] #Retrieve from array at index k
    
    # if less than 0, out of bounds
    # if greater than upper bound of array, expand array
    def __setitem__(self, position, ele):
        if not 0 <= position <self.index:
            return IndexError('desired position is out of bounds') 
        #if position >= self.capacity:
        #    self._resize(2*position) # after extending array as required, double capacity
        self.array[position] = ele
    
    # append to end of list
    def append(self, ele):
        if self.index == self.capacity:
            self._resize(2*self.capacity) #Double capacity if not enough room
        
        self.array[self.index] = ele #Set self.n index to element
        self.index += 1

    def __delitem__(self, position):
        # delete the value at that position
        # deletion position value = deletion position value + 1
        if not 0 <= position <self.index:
            return IndexError('the position you want to delete is out of bounds')
        for p in range(position, self.index - 1):
            self.array[p] = self.array[p+1]
        self.index -= 1 # should this be capacity?


    # resize array to new capacity (new_cap)     
    def _resize(self,new_cap): # a method starting with a single underscore is a private function.
        B = self.make_array(new_cap) # New bigger array
        for k in range(self.index): # Reference all existing values
            B[k] = self.array[k]
        self.array = B # Call A the new bigger array
        self.capacity = new_cap # Reset the capacity
        
    # make new array 
    def make_array(self,new_cap):
        return (new_cap * ctypes.py_object)() 

# Instantiate 
arr = DynamicArray()
# Append new element
arr.append(1)
# Check length
print("length of array : ", len(arr))
# Append new element
arr.append(2)
# Check length
print("length of array after appending 2 elements : ", len(arr))
# Append new element
arr.append(3)
# Check length
print("length of array after appending 3 elements : ", len(arr))
# Index
print("accessing element of array at index 0 : ", arr[0])
# Insert
arr[2] = 4
print(arr[2])
# Delete
del arr[1]
print(arr[1])
