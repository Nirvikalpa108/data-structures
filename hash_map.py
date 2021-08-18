from hash_map_singly_linked_list import HashMapLinkedList
# helpful documentation: https://www.interviewcake.com/concept/java/hash-map

# HashMap needs its own Node implementation in singly linked list - HashMapLinkedList

class HashMap(object):
    def __init__(self, capacity):
        array = [] # pretending this is an array with a fixed size
        self.capacity = capacity

    # turn key into a number between 0 and capacity    
    # remember - each key must be unique
    def get_hash(self, key):
        hash(key) % self.capacity # https://www.programiz.com/python-programming/methods/built-in/hash

    # add a key value pair
    def add(self, key, value):
        index = self.get_hash(key)
        if not self.array[index]: # if value at index is None
            self.array[index] = HashMapLinkedList() # create a new linked list to manage hash collisions
        self.array[index].append(key, value)

    # returns a boolean
    def contains(self, key):
        index = self.get_hash(key)
        if not self.array[index]: # if there's nothing at the index, then there's nothing to delete
            return False
        else:
            self.array[index].find(key) # the find function should output True 

    # output the value assigned to that key
    # once I've got the key Node, just call .value on it
    def get_value(self, key):
        index = self.get_hash(key)
        if not self.array[index]: # if there's no key in the array at that index, return 
            return
        else:
            self.array[index].value(key) # implement this function in HashMapLinkedList which takes a key and outputs its value 

    # delete the whole Node
    # return boolean (or value that corresponded to the key) or None if it wasn't there at all
    def delete(self, key):
        index = self.get_hash(key)
        if not self.array[index]:
            return False # if there's no key at that index, return False
        else:
            self.array[index].delete(key)

    # QUESTION
    # might be a silly question but in each array element we've initialised a HashMapLinkedList if there's a key present
    # so when we call array[index] we can call our HashMapLinkedList methods directly on that array element?

