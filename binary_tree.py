# traversals: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/ 

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
            return
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
    
    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        print(self.data)
        if self.right:
            self.right.print_in_order()

    def print_pre_order(self):
        print(self.data)
        if self.left:
            self.left.print_pre_order()
        if self.right:
            self.right.print_pre_order()

    def print_post_order(self):
        if self.left:
            self.left.print_post_order()
        if self.right:
            self.right.print_post_order()
        print(self.data)

myTree = BinaryTree()
myTree.add(1)
myTree.print_pre_order()
# this isn't working right now, I need to figure out why






