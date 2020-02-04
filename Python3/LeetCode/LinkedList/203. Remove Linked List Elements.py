# Remove all elements from a linked list of integers that have value val.
# Example:
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # M1. 特殊处理头部待删除节点
        if not head:
            return None
            
        p = head
        while p and p.val == val:
            p = p.next

        head = p
        pre = None
        while p:
            if p.val == val:
                pre.next = p.next
            else:
                pre = p
            p = p.next
        return head

        # M2. 使用dummy node处理头部待删除节点
        sentinel = ListNode(0)
        sentinel.next = head
        
        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return sentinel.next