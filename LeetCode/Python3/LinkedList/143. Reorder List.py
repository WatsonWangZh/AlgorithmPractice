# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example 1:
# Given 1->2->3->4, reorder it to 1->4->2->3.

# Example 2:
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def findMiddle(self, head):
        p2 = head
        while p2 and p2.next:
            head = head.next
            p2 = p2.next.next
        return head

    def _reverse(self,head):
        pre = None
        while head:
            curr, head = head, head.next
            #head = head.next
            curr.next, pre = pre, curr
            #pre = curr
        return pre

    def _merge(self, head, headR):
        while head.next and headR.next:
            temp1 = head.next
            temp2 = headR.next
            head.next = headR
            headR.next = temp1
            head = temp1
            headR = temp2
        return

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # 思路：分为3步：   
        # 求中点（可以先遍历找到中点，但更好的是快慢指针）
        # 翻转后面的链表
        # 两个链表合并
        if not head or not head.next:
            return
        headR = self.findMiddle(head)
        headR = self._reverse(headR)
        self._merge(head, headR)
        return

        