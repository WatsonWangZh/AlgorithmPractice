# Sort a linked list using insertion sort.

# A graphical example(https://leetcode.com/problems/insertion-sort-list/) of insertion sort. 
# The partial sorted list (black) initially contains only the first element in the list.
# With each iteration one element (red) is removed 
# from the input data and inserted in-place into the sorted list

# Algorithm of Insertion Sort:
# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, 
# finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.

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
    # 插入排序 O(n^2)
    # 为了方便处理边界情况，建立虚拟头结点，指向原链表头部。
    # 然后扫描原链表，对于每个节点 v，从前往后扫描结果链表，找到第一个比 v 大的节点 uu，将 v 插入到 u 之前。
    # 时间复杂度分析：一共遍历 n 个节点，对于每个节点找合适位置时，最多需要遍历 O(n)次，所以总时间复杂度是 O(n^2)。
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        # dummy初始化：
        dummy = ListNode(-1)
        dummy.next = head
        cursor = head.next
        head.next = None

        while cursor:
            next_cursor = cursor.next
            cursor.next = None

            # dummy.next更新的情况：
            p = dummy
            while p.next:
                if p.next.val < cursor.val:
                    p = p.next
                else:
                    cursor.next = p.next
                    p.next = cursor
                    break

            if not cursor.next:
                p.next = cursor

            cursor = next_cursor
        return dummy.next
