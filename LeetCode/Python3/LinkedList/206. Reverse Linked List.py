# Reverse a singly linked list.

# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# Follow up:
# A linked list can be reversed either iteratively or recursively.
# Could you implement both?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first, second = head, head.next
        while second:
            tmp = second.next
            second.next = first
            first, second = second, tmp
        head.next = None
        return first
