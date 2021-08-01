# https://www.geeksforgeeks.org/queue-in-python/
# Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
# Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
# Front: Get the front item from queue – Time Complexity : O(1)
# Rear: Get the last item from queue – Time Complexity : O(1)


# Custom queue implementation in Python - https://www.techiedelight.com/queue-implementation-python/
class Queue:
 
    # Initialize queue
    def __init__(self, size):
        self.q = [None] * size      # list to store queue elements
        self.capacity = size        # maximum capacity of the queue
        self.front = 0              # front points to the front element in the queue
        self.rear = -1              # rear points to the last element in the queue
        self.count = 0              # current size of the queue
 
 
    # Function to dequeue the front element
    def pop(self):
        # check for queue underflow
        if self.isEmpty():
            print("Queue Underflow!! Terminating process.")
            exit(1)
 
        print("Removing element…", self.q[self.front])
 
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1
 
 
    # Function to add an element to the queue
    def append(self, value):
        # check for queue overflow
        if self.isFull():
            print("Overflow!! Terminating process.")
            exit(1)
 
        print("Inserting element…", value)
 
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = value
        self.count = self.count + 1
 
 
    # Function to return the front element of the queue
    def peek(self):
        if self.isEmpty():
            print("Queue UnderFlow!! Terminating process.")
            exit(1)
 
        return self.q[self.front]
 
 
    # Function to return the size of the queue
    def size(self):
        return self.count
 
 
    # Function to check if the queue is empty or not
    def isEmpty(self):
        return self.size() == 0
 
 
    # Function to check if the queue is full or not
    def isFull(self):
        return self.size() == self.capacity