# https://docs.python.org/3/library/ctypes.html 
import ctypes

# https://www.geeksforgeeks.org/queue-in-python/
# enqueue - append to end of queue (if queue is full, it's called an overflow condition)
# array implementation limited due to fixed size of array
# could implement as dynamic array - Big O not great due to doubling

# pop - dequeue the front element (remove item, it's called underflow if there's nothing there)
# peek (return front item)
# peek for last element?
# isEmpty
# isFull
# size

# THIS IS A QUEUE BACKED BY AN ARRAY - IT'S EASIER USING A LINKED LIST

class Queue(object):
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = 10
        self.array = self.make_array(self.capacity)
    
    def __str__(self):
        if self.size == 0:
            return "I'm empty"
        else:
            return "I am a queue with " + str(self.size) + " elements"
    
    # remember, first in first out - incrementing the tail to point to nothing, that's cool. the head is in the right place.
    def enqueue(self, value):
        if self.size != self.capacity: # we can't add to the queue if it's already full (so can't overwrite)
            self.array[self.tail] = value
            if self.tail + 1 == self.capacity: # if we are at capacity
                self.tail = 0 # reset the tail pointer to 0 (we'll only do this, if the array is not full)
            else:
                self.tail += 1 # increment the tail pointer
            self.size += 1 # in either case, increment the size counter

    
    # make new array 
    def make_array(self,new_cap):
        return (new_cap * ctypes.py_object)() 




