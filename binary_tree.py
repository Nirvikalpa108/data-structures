# traversals: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/ 
# https://algorithms.tutorialhorizon.com/inorder-predecessor-and-successor-in-binary-search-tree/
# https://www.geeksforgeeks.org/inorder-predecessor-successor-given-key-bst/

# delete function explanation
# https://www.youtube.com/watch?v=i2s4Tyw3_dY
# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
# The worst case time complexity of delete operation is O(h) 
# where h is the height of the Binary Search Tree. 
# In worst case, we may have to travel from the root to the deepest leaf node. 
# The height of a skewed tree may become n and the time complexity of delete operation may become O(n)

# a h/w for another day is to re-write the traversal functions using iterative methods on the tree (similar to find)
# here are the iterative implementations I found online. They all use a stack.
# https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/
# https://www.techiedelight.com/preorder-tree-traversal-iterative-recursive/ 
# https://www.techiedelight.com/postorder-tree-traversal-iterative-recursive/ 


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
    
    # assuming there is a right child (see predecessor function for left child)
    def successor(self, node):
        if node.right:
            return self.find_min(node.right)
        else:
            raise Exception # haven't implemented the case where there isn't a right child yet 


    def find_min(self, node): # get minimum value from left children
        current = node
        while current.left:
            current = current.left
        return current  
    
    # assuming there is a left child
    def predecessor(self, node):
        if node.left:
            return self.find_max(node.left)
        else:
            raise Exception # haven't implemented the case where there isn't a left child yet 

    def find_max(self, node): # get max value from right children
        current = node
        while current.right:
            current = current.right
        return current  

    # Q - what should this function return???? 
    # (https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/ returns root node or None, so could be a possibility)
    def delete(self, value):
        # find the Node by looking for its value in the tree
        nodeToDelete = self.find_node(value) 
        if not nodeToDelete: # if None, the tree is empty
            return False
        else:
            # are you a leaf node? delete me, no big deal
            if nodeToDelete.isLeaf():
                # but before I do that, which child am I?
                if nodeToDelete == nodeToDelete.parent.right:
                    nodeToDelete.parent.right = None
                else:
                    nodeToDelete.parent.left = None
            # do you have 1 child?
            elif nodeToDelete.right and not nodeToDelete.left:
                # find out what I am to my parent (am I the left or right child?)
                # modify parent to point to the right child
                if nodeToDelete == nodeToDelete.parent.right:
                    nodeToDelete.parent.right = nodeToDelete.right
                else:
                    nodeToDelete.parent.left = nodeToDelete.right
            elif nodeToDelete.left and not nodeToDelete.right:
                # find out what I am to my parent (am I the left or right child?)
                # modify parent to point to the left child
                if nodeToDelete == nodeToDelete.parent.left:
                    nodeToDelete.parent.left = nodeToDelete.left
                else:
                    nodeToDelete.parent.right = nodeToDelete.left
            # do you have 2 children? Then return the successor.
            else:              
                # find successor (the successor function assumes there is a right child)
                sucessor = self.successor(nodeToDelete)
                # if successor is direct right child of nodeToDelete,
                if sucessor == nodeToDelete.right:
                    # find out which child I am to my parent
                    # if I was the left child to my parent,
                    # then set my parent's left child to my successor
                    if nodeToDelete == nodeToDelete.parent.left:
                        nodeToDelete.parent.left = sucessor

                    else:
                        nodeToDelete.parent.right = sucessor
                # else, successor is somewhere in the right subtree but not right child
                else:
                    # replace successor by its own right child
                    sucessor = sucessor.right
                    # replace nodeToDelete with successor
                    nodeToDelete = sucessor
    
    # https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
    def deleteAgain(self, root, value):
        
        # if the tree is empty OR we don't find the value, return None
        if not root:
            return root
        
        # now, we're looking for the subtree where the value is the root of that subtree
        # if value is less than root, look in the left subtree
        elif value < root.data:
            root.left = self.deleteAgain(root.left, value)

        # if value is greater than root, look in the right subtree   
        elif value > root.data:
            root.right = self.deleteAgain(root.right, value)
        
        # now we have found the right subtree and the root of it is the node to delete
        else:
            # it's a leaf - no children
            if root.isLeaf():
                return None  

            # 1 child - so we just need to return that child, just like above - sthg to do wth the recursion
            # 2 conditions - left or right tree
            elif not root.left:
                root = root.right
            
            elif not root.right:
                root = root.left
            
            # 2 children
            else:
                # find the minimum value in the tree.
                minValueOfRightSubtree = self.find_min(root)
                # copy the minimum value to the root
                root.value = minValueOfRightSubtree
                # now delete the min value that has already been copied to root (we don't want the value occuring twice in the tree)
                root.right = self.deleteAgain(root.right, minValueOfRightSubtree.value)
        return root


    

myTree = BinaryTree()
myTree.add(2)
myTree.add(1)
myTree.add(5)
myTree.add(7)
myTree.add(4)
myTree.root.print_in_order()
print("about to delete")
myTree.delete(5)
print("completed deletion, about to print again")
myTree.root.print_in_order()
print("completed print attempt")






