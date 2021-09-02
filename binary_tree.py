# traversals: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/ 

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)
    
    # is the value == node? if not, 
    # if value < root, go to the left child
    # if value > root, go to right child
    def find(self, value):
        if value < self.data:
            return self.left.find(value)
        elif value > self.data:
            return self.right.find(value)
        else: 
            return True #self.data == value
    
    # build a string, so that prints on one line. 
    # right now we're not returning a string, just printing
    def print_in_order(self): # outputs the numbers in order
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
    
    # iterative implementation - loop changing pointers
    # recursion is not infinite (stack overflow), so iteration is important to learn
    def find(self, value):
        current = self.root
        while current != None:
            if value < current.data:
                current = current.left
            elif value > current.data:
                current = current.right
            else: 
                return True 
        return False # current is equal to None, we've reached end of tree
    
    # h/w - find an image (video?) of deleting a Node in a tree
    # re-write the traversal functions using iterative methods on the tree (similar to find)

myTree = BinaryTree()
myTree.add(2)
myTree.add(1)
myTree.add(3)
myTree.root.print_in_order()






