# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Example 1:
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL

# Example 2:
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 链表为空或者只有一个结点
        if not head or not head.next:
            return head
        # 统计链表长度
        cur = head
        count = 0
        while cur!=None:
            count += 1
            cur = cur.next
        # 控制k的范围
        k = k % count
        if k==0:
            return head
        # 双指针找边界
        first = head
        second = head
        for i in range(k):
            first = first.next
        while first.next!=None:
            first = first.next
            second = second.next
        # 改变链接关系
        first.next = head
        head = second.next
        second.next = None
        return head
