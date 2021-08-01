# class that represents a Node element
class Node(object):
    # __init__ for that node (data value, pointer forwards, pointer backwards)
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    # __repr__ (string representation)
    def __repr__(self):
        return str(self.data)

# class for doubly linked list
class DoublyLinkedList(object):
    # __init__ function
    def __init__(self):
        self.head = None
        # self.tail = None ---> CONFIRMED WITH JORDAN THIS ISN'T A STANDARD IMPLEMENTATION 
    
    # __repr__ function
    def __repr__(self):
        if not self.head:
            return "I can't print an empty list mate"
        output = self.head
        curr = self.head
        while curr:
            curr = curr.next
            output = str(output) + " -> " + str(curr)
        return output

    def prepend(self, value):
        # if the list is not empty:
        if self.head:
            newNode = Node(value, None, self.head) # make the newNode with a prev of None and a next of  self.head
            self.head.prev = newNode # make the current head of the list's prev point to NewNode
            self.head = newNode
        # if the list is empty:
        else:
            self.head = Node(value, None, None)

    def append(self, value):
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            newNode = Node(value, curr, None)
            curr.next = newNode
        else:
            self.head = Node(value, None, None)
    
    # prepend where the doubly linked list has a pointer to the tail 
    # (we implemented this first time around thinking it was a standard feature, but turns out it's not so look at prepend!)
    def prependWithTailReference(self, value):
        newNode = Node(value, None, self.head)
        if not self.tail: # if list is empty (because tail defaults to None)
            self.tail = newNode
        if self.head: # if we do have a head
            self.head.prev = newNode
        self.head = newNode

    # append where the doubly linked list has a pointer to the tail 
    def appendWithTailReference(self, value):
        newNode = Node(value, self.tail, None)
        if not self.head: # if list is empty
            self.head = newNode
        if self.tail: # check tail is not None (or we haven't set a tail, which defaults to None)
            self.tail.next = newNode
        self.tail = newNode

    # find (return None if not found)
    def find(self, value):
        if not self.head: # if list is empty, return false 
            return False 
        
        curr = self.head
        while curr.next and curr.data != value:
            curr = curr.next
        return curr.data == value

    # delete (find element and keep reference to element preceding it, unlink it from the list)
    def delete(self, value):
        # if list is empty, do nothing
        if not self.head:
            pass
        # check each element in the list
        else:
            curr = self.head
            while curr.next and curr.data != value: # if data is not equal to value, keep iterating
                curr = curr.next
            if curr.data == value: # if data is equal to value, hook the prev and next nodes together
                prev = curr.prev
                next = curr.next
                prev.next = next
                next.prev = prev

    # reverse list
    def reverse(self):
        if not self.head:
            pass
        else:
            curr = self.head
            # iterate over each element
            while curr.next:
                # switch the prev and next pointers around
                prev = curr.prev
                next = curr.next
                curr.prev = next 
                curr.next = prev
                curr = next
            # we're now at the last element, so do the final switch of the prev pointer
            prev = curr.prev
            curr.next = prev
            # then initialise the list with it's new head
            self.head = curr

list = DoublyLinkedList()
print(list.find(2))
list.prepend(2)
print(list)
list.prepend(1)
print(list)
list.append(3)
print(list)
list.append(4)
print(list)
print(list.find(3))
list.delete(5)
print(list)
list.reverse()
print(list)