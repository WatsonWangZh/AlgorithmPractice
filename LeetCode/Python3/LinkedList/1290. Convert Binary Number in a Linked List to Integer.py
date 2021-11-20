# Given head which is a reference node to a singly-linked list. 
# The value of each node in the linked list is either 0 or 1. 
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.

# Example 1:
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

# Example 2:
# Input: head = [0]
# Output: 0

# Example 3:
# Input: head = [1]
# Output: 1

# Example 4:
# Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# Output: 18880

# Example 5:
# Input: head = [0,0]
# Output: 0

# Constraints:
# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.

# Hints:
# Traverse the linked list and store all values in a string or array. 
# convert the values obtained to decimal value.
# You can solve the problem in O(1) memory using bits operation. 
# use shift left operation ( << ) and or operation ( | ) to get the decimal value in one operation.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        # M1. 模拟
        res = 0 
        while head:
            res = res * 2 + head.val
            head = head.next
        return res

        # M2. 模拟
        res = 0 
        while head:
            res = res << 1 | head.val
            head = head.next
        return res
