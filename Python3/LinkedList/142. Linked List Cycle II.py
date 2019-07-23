# Given a linked list, return the node where the cycle begins. 
# If there is no cycle, return null.
# To represent a cycle in the given linked list, 
# we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
# If pos is -1, then there is no cycle in the linked list.
# Note: Do not modify the linked list.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Example 2:
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Example 3:
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.

# Follow-up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 龟兔赛跑，快慢指针法
        # 动画演示：https://hui-wang.info/2017/11/18/%E5%8A%A8%E7%94%BB%E8%A7%A3%E9%87%8A%E5%A6%82%E4%BD%95%E6%B1%82%E5%8D%95%E9%93%BE%E8%A1%A8%E7%8E%AF%E5%85%A5%E5%8F%A3%E7%82%B9/
        # 理论证明：http://wuchong.me/blog/2014/03/25/interview-link-questions/
        fast = slow = head
        while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                # if there is cycle:
                if slow == fast:
                    #the head and slow nodes move step by step
                    while head:
                        if head == slow:
                                return head
                        head = head.next
                        slow = slow.next
        return None
