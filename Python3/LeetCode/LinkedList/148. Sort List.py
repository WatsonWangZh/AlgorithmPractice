# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:
# Input: 4->2->1->3
# Output: 1->2->3->4

# Example 2:
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 转载自 http://zxi.mytechroad.com/blog/list/leetcode-148-sort-list/
        # M1.Top-down (recursion)
        # Time complexity: O(nlogn)
        # Space complexity: O(logn) 可以通过,但不满足题目空间复杂度为O(1)的要求
        # def merge(l1, l2):
        #     dummy = ListNode(0)
        #     tail = dummy
        #     while l1 and l2:
        #         if l1.val > l2.val: l1, l2 = l2, l1
        #         tail.next = l1
        #         l1 = l1.next
        #         tail = tail.next
        #     tail.next = l1 if l1 else l2
        #     return dummy.next
            
        # if not head or not head.next: 
        #     return head
        # slow = head
        # fast = head.next
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        # mid = slow.next
        # slow.next = None
        # return merge(self.sortList(head), self.sortList(mid))



        # https://leetcode.com/problems/sort-list/discuss/46838/Python-bottom-up-O(nlogn)-time-O(1)-space-solution
        # M2.Bottom-up
        # Time complexity: O(nlogn)
        # Space complexity: O(1)
        
        if not head or not head.next: 
            return head

        dummy = ListNode(0) 
        dummy.next = head

        tmp = head
        length = 0
        while tmp:
            tmp = tmp.next
            length += 1

        step = 1
        while step < length:
            cur, tail = dummy.next, dummy
            while cur:
                left = cur
                right = self.split(left,step)
                cur = self.split(right, step)
                tail = self.merge2(left,right,tail)
            step <<= 1
        return dummy.next
    
    # merge 2 sorted lists, and append the result to head
    # return the tail
    def merge2(self, p1, p2, head):
        dummy = ListNode(0)
        p = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next; p = p.next
            else:
                p.next = p2
                p2 = p2.next; p = p.next
        p.next = p1 or p2
        head.next = dummy.next
        while p.next: p = p.next
        return p

    # divide the linked list into two lists
    # first linked list contains n nodes
    # return the head of second linked list
    def split(self, head, n):
        for i in range(n-1): 
            if head: head = head.next
            else: break
        if not head: return None
        second = head.next
        head.next = None
        return second
