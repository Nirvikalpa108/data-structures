# https://en.wikibooks.org/wiki/Data_Structures/Stacks_and_Queues#Stacks
# https://www.geeksforgeeks.org/stack-in-python/

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

class Stack(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        if not self.head:
            return "empty stack"
        return "stack of size " + str(self.size) + " with top element = " + str(self.head)
    
    def push(self, value):
        self.head = Node(value, self.head)
        self.size += 1

    # remove head value and retrieve
    def pop(self):
        if not self.head:
            return None
        else:
            oldHead = self.head
            next = oldHead.next
            self.head = next
            self.size -= 1
            return oldHead.data
    
    def peek(self):
        return self.head.data

    def empty(self):
        return not self.head
    
    def size(self):
        return self.size
    
newStack = Stack()
print(newStack.empty())
print(newStack)
print(newStack.pop())
newStack.push(1)
print(newStack)
newStack.push(2)
print(newStack)
print(newStack.pop())
print(newStack)
print(newStack.empty())
