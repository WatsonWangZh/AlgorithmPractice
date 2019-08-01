# Reverse a linked list from position m to n. Do it in one-pass.
# Note: 1 ≤ m ≤ n ≤ length of list.

# Example:
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        dummy = ListNode(0)
        dummy.next = head

        p = dummy
        for i in range(m-1):
            p = p.next

        p1 = p.next
        p2 = p1.next
        for j in range(n-m):
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp

        p.next.next = p2
        p.next = p1
        
        return dummy.next
