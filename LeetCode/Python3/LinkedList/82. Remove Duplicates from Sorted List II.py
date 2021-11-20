# Given a sorted linked list, delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list.

# Example 1:
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5

# Example 2:
# Input: 1->1->1->2->3
# Output: 2->3

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # M1.递归
        # if not head or not head.next:
        #     return head
        # p = head.next
        # if p.val != head.val:
        #     head.next = self.deleteDuplicates(p)
        #     return head
        # else:
        #     while p and p.val==head.val:
        #         p = p.next
        #     return self.deleteDuplicates(p)

        # M2.双指针
        # 空链表或者只有一个节点
        if not head or not head.next:
            return head
        # 避免链表删空时的复杂判断
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        while prev.next:
            is_repeated = False
            while prev.next.next and prev.next.val == prev.next.next.val:
                prev.next = prev.next.next
                is_repeated = True
            if is_repeated:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next
                
