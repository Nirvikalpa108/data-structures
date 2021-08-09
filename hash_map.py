from singly_linked_list import SinglyLinkedList
# helpful documentation: https://www.interviewcake.com/concept/java/hash-map
# def __init__(self) - set the size of the array
# def get_hash(self, key) - takes a key and generates an appropriate index to assign that key
# def add(self, key, value) - adds a value to a key (calls the get_hash function)
# def get(self, key) - gets a value (or values?) - calls get_hash
# def delete(self, key) - delete a key 
# def keys(self) - list all the keys


# HashSet has keys, no values
class HashSet(object):
    def __init__(self, capacity):
        array = [] # pretending this is an array with a fixed size. use the ctypes library later to implement from scratch.
        self.capacity = capacity
    
    # turn key into a number between 0 and capacity    
    # make an assumption about the type of key (int perhaps. we could always use python's hash function to turn x into an int)
    # easiest hash function - hash(key) % capacity (https://www.programiz.com/python-programming/methods/built-in/hash)
    def get_hash(self, key):
        pass
    
    def add(self, key):
        index = self.get_hash(key)
        if not self.array[index]: # if value at this index is None
            self.array[index] = SinglyLinkedList() # Q - in the interview, which linked list implementation should I use? (I can't see an appropriate python one)
        self.array[index].append(key)

    # returns a boolean
    def contains(self, key):
        # apply hash function to key to get the index
        index = self.get_hash(key)
        # if there's nothing at that index, return false
        return self.array[index]

    def delete(self, key):
        # apply hash function to key to get the index
        index = self.get_hash(key)
        # delete the key at that index
        self.delete(index) # does this work?!

    # Q - double check it's ok for me to use all these built in array methods?

    # 

