# traversals: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/ 

class Node(object):
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

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
    
    def isLeaf(self):
        # this returns True if the Node doesn't have a left and right child
        return not self.left and not self.right

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def __str__(self):
        pass

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            self.root.parent = None
            return
        currentParent = self.root # we have a root, so we can make it a parent
        while True: # this will loop until we return out 
            if value < currentParent.data:
                if currentParent.left:
                    currentParent = currentParent.left
                else: # if left child is None
                    currentParent.left = Node(value, parent=currentParent)
                    return
            elif value > currentParent.data:
                if currentParent.right:
                    currentParent = currentParent.right
                else: 
                    currentParent.right = Node(value, parent=currentParent)
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

    
    # 9/9/21 - I tried the iterative traversals by myself and then i saw that they all use a stack. i haven't implemented it with a stack yet

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
            current = current.left
            if current.right:
                result + str(current.right)
                current = current.right
        return result 

    # 16/9/21 h/w - write stack implementations and discuss

    # 9/9/21 h/w - find an image (video?) of deleting a Node in a tree
    # https://www.youtube.com/watch?v=i2s4Tyw3_dY
    # https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
    # The worst case time complexity of delete operation is O(h) where h is the height of the Binary Search Tree. 
    # In worst case, we may have to travel from the root to the deepest leaf node. The height of a skewed tree may become n and the time complexity of delete operation may become O(n)
    # the basic idea for delete is that there are three possibilities
    # I am a leaf node - just delete me, no big deal
    # I have one child node - copy single child to node and then delete
    # I have two children - find out which node should replace it, could be below the children too. Copy it to node and then delete.
    # what does this mean??? The important thing to note is, inorder successor is needed only when the right child is not empty. 
    # In this particular case, inorder successor can be obtained by finding the minimum value in the right child of the node.

    # returns Node
    def find_node(self, value):
        current = self.root
        while current != None:
            if value < current.data:
                current = current.left
            elif value > current.data:
                current = current.right
            else: 
                return current 
        return None # current is equal to None, we've reached end of tree

    def delete(self, value):
        #determine where/what is this value
        nodeToDelete = self.find_node(value) 
        if not nodeToDelete: # if this is None, the tree is empty
            return False
        else:
            # are you a leaf node? delete me, no big deal
            if nodeToDelete.isLeaf():
                # first, which child am I?
                if nodeToDelete == nodeToDelete.parent.right:
                    nodeToDelete.parent.right = None
                else:
                    nodeToDelete.parent.left = None
            # do you have 1 child?
            elif nodeToDelete.right and not nodeToDelete.left:
                pass
            elif nodeToDelete.left and not nodeToDelete.right:
                pass
            # do you have 2 children?
            else:
                pass
        pass

    # h/w definition of successor and predecessor
    # https://algorithms.tutorialhorizon.com/inorder-predecessor-and-successor-in-binary-search-tree/
    # it's just the next number (lower and higher) - and it's about finding that number so you can do the right replacement
    # https://www.geeksforgeeks.org/inorder-predecessor-successor-given-key-bst/


    # h/w - for delete, add the function definitions with types they will return 
    # https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/ 
    # given a non-empty BST, search tree, return node with minimum key value. 
    # find the leftmost leaf
    # returns node
    def min_value_node(node):
        pass
    # delete node and return new BST root
    def delete(self, key):
        # Base case - if root is None, return None
        # if key to delete is smaller than root, then its in left subtree (recurse with the left child of root)
        # if key to delete is greater than root, then its in right subtree (recurse with the right child of root)
        # if key is same as root, then delete root node
            # if node has one child or no child
            # if node has two children, get inorder successor (call min_value_node to get smallest in right subtree)
            # copy inorder successor to root
            # delete inorder successor (use recursion)
        pass


myTree = BinaryTree()
myTree.add(2)
myTree.add(1)
myTree.add(3)
myTree.root.print_in_order()
myTree.print_in_order()






