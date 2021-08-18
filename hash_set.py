from singly_linked_list import SinglyLinkedList
# helpful documentation: https://www.interviewcake.com/concept/java/hash-map

# HashSet has keys, no values
class HashSet(object):
    def __init__(self, capacity):
        array = [] # pretending this is an array with a fixed size. 
        self.capacity = capacity
    
    # turn key into a number between 0 and capacity    
    # remember - each key must be unique
    def get_hash(self, key):
        hash(key) % self.capacity # https://www.programiz.com/python-programming/methods/built-in/hash
    
    def add(self, key):
        index = self.get_hash(key)
        if not self.array[index]: # if value at this index is None
            self.array[index] = SinglyLinkedList() # Q - in the interview, which linked list implementation should I use? (can just use pseudo code)
        self.array[index].append(key)

    # returns a boolean
    def contains(self, key):
        # apply hash function to key to get the index
        index = self.get_hash(key)
        # if there's nothing at that index, return false
        if not self.array[index]: # if value at this index is None
            return False
        else:
            return self.array[index].find(key) # using my implementation. in the interview, pseudo code it and explain.

    # could write this outputing a boolean next time
    def delete(self, key):
        # apply hash function to key to get the index
        index = self.get_hash(key)
        if not self.array[index]: # if value at this index is None, there's nothing to delete
            return # matching output of singly linked list delete function implementation (pass is same as return)
        else:
            # delete the key at that index
            self.array[index].delete # using my implementation. in the interview, pseudo code it and explain.

    # Amina - could do this later
    def keys(self): # list keys in an array
        pass

