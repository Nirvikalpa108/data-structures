# can't print - how to test?
    # different ways of walking the tree 
        # in order - print all left children and then print all right
        # pre and post order too

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def __str__(self):
        pass

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        parent = self.root
        while True: # this will loop until we return out 
            if value < parent.data:
                if parent.left:
                    parent = parent.left
                else: # if left child is None
                    parent.left = Node(value)
                    return
            elif value > parent.data:
                if parent.right:
                    parent = parent.right
                else: 
                    parent.right = Node(value)
                    return 
            else:
                raise ValueError("no duplicate values allowed") 

# h/w - try an in-order print of the tree on the jordan jamboard


