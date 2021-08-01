# implementing queue with a singly linked list - very easy
# not so easy with a non dynamic array - see the other file for that attempt

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        if not self.head:
            return "empty queue"
        else:
            return "The head is " + str(self.head) + " and the tail is " + str(self.tail)
    
    # add a value to the tail and increment tail pointer
    def enqueue(self, value):
        newNode = Node(value, None) # new tail of the list, so it points to None
        
        if not self.head:
            self.head = newNode # is this correct? should the new node be the head AND the tail?
        else:
            self.tail.next = newNode # point the current tail to the new node
        
        self.tail = newNode # make the new node the new tail
        self.size += 1 # increment the size pointer 

    # remove head value and retrieve
    def dequeue(self):
        if not self.head:
            return None
        else:
            oldHead = self.head
            newHead = self.head.next
            self.head = newHead
            self.size -= 1
            return oldHead

    # peek (return front item)
    def peek(self):
        return self.head

    # isEmpty
    def isEmpty(self):
        return not self.head #Amina, try to remember this syntax

    def size(self):
        return self.size # QUESTION - I feel like this function isn't actually being called
        # It says INT object is not callable?

newQueue = Queue()
print(newQueue)
print(newQueue.isEmpty())
print(newQueue.size)
newQueue.enqueue(1)
print(newQueue)
newQueue.enqueue(2)
print(newQueue)
print(newQueue.size)
newQueue.dequeue()
print(newQueue)
print(newQueue.head)
print(newQueue.isEmpty())
print(newQueue.size)
