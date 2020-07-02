# Write a program to find the node at which 
# the intersection of two singly linked lists begins.

# Example 1:
# A:    4->1->8->4->5
# B: 5->0->1->8->4->5
# Input: intersectVal = 8, listA = [4,1,8,4,5], 
# listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 
# (note that this must not be 0 if the two lists intersect). 
# From the head of A, it reads as [4,1,8,4,5]. 
# From the head of B, it reads as [5,0,1,8,4,5]. 
# There are 2 nodes before the intersected node in A; 
# There are 3 nodes before the intersected node in B.

# Example 2:
# A: 2->6->4
# B: 1->5
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], 
# skipA = 3, skipB = 2
# Output: null
# Input Explanation: From the head of A, it reads as [2,6,4]. 
# From the head of B, it reads as [1,5]. 
# Since the two lists do not intersect, intersectVal must be 0, 
# while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Some trick funny
        if not headA or not headB:
            return None
        # two pointer
        a, b = headA, headB
        while a is not b:
            # if either pointer hits the end, switch head and continue the second traversal
            # if not hit the end, just move on to the next
            a = a.next if a else headB
            b = b.next if b else headA
        return a

