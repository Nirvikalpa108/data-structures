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

    
    # 9/9/21 - I watched a video on deletion and read about it
    # I tried the iterative traversals by myself and then i saw that they all use a stack. i haven't implemented it with a stack yet

    # re-write the traversal functions using iterative methods on the tree (similar to find)
    # here are the iterative implementations I found online. They all use a stack.
    # https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/
    # https://www.techiedelight.com/preorder-tree-traversal-iterative-recursive/ 
    # https://www.techiedelight.com/postorder-tree-traversal-iterative-recursive/ 

    # this is what I was initially thinking before I googled
    def print_in_order(self): 
        current = self.root
        while current != None:
            result = ""
            if current.left:
                result + str(current.left)
            result + str(current.data)
            if current.right:
                result + str(current.right)
        return result 

    # h/w - find an image (video?) of deleting a Node in a tree
    # https://www.youtube.com/watch?v=i2s4Tyw3_dY
    # https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
    # The worst case time complexity of delete operation is O(h) where h is the height of the Binary Search Tree. In worst case, we may have to travel from the root to the deepest leaf node. The height of a skewed tree may become n and the time complexity of delete operation may become O(n)
    # the basic idea for delete is that there are three possibilities
    # I am a leaf node - just delete me, no big deal
    # I have one child node - copy single child to node and then delete
    # I have two children - find out which node should replace it, could be below the children too. Copy it to node and then delete.
    # what does this mean??? The important thing to note is, inorder successor is needed only when the right child is not empty. In this particular case, inorder successor can be obtained by finding the minimum value in the right child of the node.

myTree = BinaryTree()
myTree.add(2)
myTree.add(1)
myTree.add(3)
myTree.root.print_in_order()
myTree.print_in_order()






