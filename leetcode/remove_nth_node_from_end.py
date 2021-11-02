# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/ 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if list is empty, return None (Q - is this the right return type??)
        if not head:
            return None
        # if list is not empty
        else:
            # create a counter and 3 pointers; current Node, nodeToRemove & nodeToRemovePrev
            # the counter tells us when to start iterating the nodeToRemove & nodeToRemovePrev, which stay at the head until  
            # they're at the correct range (n) from the current pointer (which will eventually point to tail)
            counter = 0
            current = head
            nodeToRemove = head
            # adding this pointer so it's easy to run the delete operation
            nodeToRemovePrev = head
            while current.next:
                current = current.next
                counter += 1
                if counter >= n:
                    nodeToRemove = nodeToRemove.next
                if counter >= n+1: 
                    nodeToRemovePrev = nodeToRemovePrev.next
                    
            # if the head is the nodeToRemove, make head.next the head of the list
            if head == nodeToRemove:
                newHead = head.next
                head = None
                return newHead
            else:
                # to delete nodeToRemove, change the pointer of nodeToRemovePrev to nodeToRemove.next
                nodeToRemovePrev.next = nodeToRemove.next
                # return the head of the list like the question requires
                return head