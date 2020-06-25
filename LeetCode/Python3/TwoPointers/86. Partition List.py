# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

# Example:
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # M1. 模拟
        # 首先找到第一个大于或等于给定值的节点cur
        # 然后再找小于给定值的节点，每找到一个就将其取出置于cur之前即可

        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head

        while pre.next and pre.next.val < x:
            pre = pre.next
        cur = pre

        while cur.next:
            if cur.next.val < x:
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
                pre = pre.next
            else:
                cur = cur.next
        return dummy.next

        # M2. 划分合并
        # 将小于给定值和大于给定值的节点分别按原始先后顺序划分到两个链表中
        # 然后再拼接成最后的结果返回即可

        small_dummy, big_dummy = ListNode(0), ListNode(0)
        small_cur, big_cur = small_dummy, big_dummy
        while head:
            if head.val < x:
                small_cur.next = head
                small_cur = head
            else:
                big_cur.next = head
                big_cur = head
            head = head.next
            
        big_cur.next = None
        small_cur.next = big_dummy.next
        return small_dummy.next