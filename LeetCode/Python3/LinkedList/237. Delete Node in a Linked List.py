# Write a function to delete a node (except the tail) 
# in a singly linked list, given only access to that node.

# Example 1:
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, 
# the linked list should become 4 -> 1 -> 9 after calling your function.

# Example 2:
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, 
# the linked list should become 4 -> 5 -> 9 after calling your function.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 用其后结点值覆盖待删除结点，然后删除待删除结点的下一个结点，达到效果
        node.val = node.next.val
        node.next = node.next.next

        