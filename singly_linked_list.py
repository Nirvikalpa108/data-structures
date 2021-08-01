# class that represents a Node element
class Node(object):
    # an __init__ function for that node (data value and pointer)
    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next

    def __str__(self):
        return str(self.data)

# class for the singly linked list
class SingleLinkedList(object):
    # __init__ function
    def __init__(self):
        self.head = None
    
    def __str__(self):
        if not self.head:
            return "this is an empty linked list"

        result = str(self.head)
        currentEl = self.head
        while currentEl:
            currentEl = currentEl.next
            result = result + " -> " + str(currentEl)

        return result

    # prepend
    def prepend(self, value):
        self.head = Node(value, self.head) 
    
    # append 
    def append(self, value):
        newNode = Node(value, None)

        if not self.head: # if head is
            self.head = newNode
        else: # if head is not empty, do this
            currentEl = self.head
            while currentEl.next: # if a currentEl.next exists
                currentEl = currentEl.next 

            currentEl.next = newNode
    
    # find (return true if present and false otherwise)
    def find(self, value):
        if not self.head: # if linked list is empty
            return False 
        
        currentEl = self.head
        while currentEl.next and currentEl.data != value: # if a CurrentEl.next exists AND the currentEl does not equal the value we're looking for, keep looping
            currentEl = currentEl.next
        return currentEl.data == value 

    def reverseAgain(self): # I did this one kind of by myself. Struggling to understand why we need to assign next first in the loop.
        current = self.head
        prev = None
        while current != None:
            next = current.next # stash the next value for later
            current.next = prev # switch the pointer backwards
            prev = current # move the previous along one   
            current = next # move the current along one     
        self.head = prev
    
    # AMINA AP - GO THROUGH THIS ON PAPER AND CODE IT BY MYSELF AGAIN TO MAKE SURE I FULLY UNDERSTAND
    def reverse(self):
        # 1,2,3
        currentEl = self.head # 1
        previousEl = None # None
        while currentEl.next: # until we get to the end
            nextEl = currentEl.next # next = 2
            currentEl.next = previousEl # 
            previousEl = currentEl
            currentEl = nextEl
        currentEl.next = previousEl
        self.head = currentEl

    # delete (find element and keep reference to element preceding it, unlink it from the list)
    # Q - what happens if we have 2 values that we want to delete? (consider doing some if work inside while loop)
    def delete(self, value):
        current = self.head
        while current.next and current.data != value: # where current element does not hold the value
            previous = current # set the current el to be the previous one
            current = current.next # and then look at the next element 
            next = current.next # omg i think im going crazy, is this right?? is this the next element?
            if current.data == value:
                current.next = None # remove the pointer from current el
                previous.next = next # make the previous el point to the el after the current el that we just deleted (goodness this is confusing)
                current = next
            else:
                pass # if we don't find the element to delete, dont modify the linked list

    # remove ONE element from linked list
    def deleteAgain(self, value):
        current = self.head
        prev = None

        # if the head equals the value we want to delete, we need to re-assign the head of our linked list
        if current.data == value: # do I also need to check somehwere that we are not dealing with an empty list?
            next = current.next # get the next value along
            current.next = None #unhook the pointer
            self.head = next # set the new head of the list
            return # remember, we're only removing 1 element from the list

        while current != None: # check this compiles
            next = current.next
            if current.data == value:
                current.next = None #unhook pointer
                prev.next = next #put correct pointer
                return 
            else: 
                prev = current
                current = next #iterate along and go back into the while loop

    def deleteAgainReturnBoolean(self, value):
        # iterate through the list
        # is this current value, the one that 
        pass

myList = SingleLinkedList()
myList.prepend(3)
myList.prepend(2)
myList.prepend(2)
myList.prepend(1)
print(myList)
myList.reverseAgain()
print(myList)
