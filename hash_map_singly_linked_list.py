
# each Node holds a key, value and a pointer to the next
class Node(object):
    # an __init__ function for that node (data value and pointer)
    def __init__(self, key=None, value=None, next=None):
        self.key = key,
        self.value = value 
        self.next = next

# class for the singly linked list
class HashMapLinkedList(object):
    # __init__ function
    def __init__(self):
        self.head = None
    
    # append a key value pair to the list
    def append(self, key, value):
        newNode = Node(key, value, None)
        # if the list is empty, make this Node the head of it
        if not self.head:
            self.head = newNode
        # otherwise, iterate through the list until you get to the last node
        # assign the last node's next to our new node, to append it to the list
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    # output boolean
    def find(self, key):
        # if the list is empty, return False
        if not self.head:
            return False
        else:
            current = self.head
            while current.next and current.data != key:
                current = current.next
            return current.data == key

    # output value for given key
    # is this correct?
    def get_value(self, key):
        # if list is empty, return out
        if not self.head:
            return
        else:
            current = self.head
            while current.next and current.data != key:
                current = current.next
            if current.data:
                current.value
            else:
                return 

    # output a boolean
    def delete(self, key):
        if not self.head:
            return False
        else:
            current = self.head
            prev = None
            # if head is key to be deleted, reassign head of list
            if current.key == key:
                next = current.next # hold the next value along
                current.next = None # unhook the pointer
                self.head = next # set the new head of the list
                return True 
            else:
                while current.next:
                    next = current.next
                    if current.key == key:
                        current.next = None # unhook the pointer
                        prev.next = next #put correct pointer
                        return True
                    else:
                        prev = current
                        current = next #iterate along and go back into the while loop

