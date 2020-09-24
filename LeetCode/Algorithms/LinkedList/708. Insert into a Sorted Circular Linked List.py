# Given a node from a Circular Linked List which is sorted in ascending order, 
# write a function to insert a value insertVal into the list such that it remains a sorted circular list. 
# The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the circular list.
# If there are multiple suitable places for insertion, 
# you may choose any place to insert the new value. 
# After the insertion, the circular list should remain sorted.
# If the list is empty (i.e., given node is null), 
# you should create a new single circular list and return the reference to that single node. 
# Otherwise, you should return the original given node.

# Example 1:
# Input: head = [3,4,1], insertVal = 2
# Output: [3,4,1,2]
# Explanation: In the figure above, there is a sorted circular list of three elements. 
# You are given a reference to the node with value 3, and we need to insert 2 into the list. 
# The new node should be inserted between node 1 and node 3. 
# After the insertion, the list should look like this, and we should still return node 3.

# Example 2:
# Input: head = [], insertVal = 1
# Output: [1]
# Explanation: The list is empty (given head is null). 
# We create a new single circular list and return the reference to that single node.

# Example 3:
# Input: head = [1], insertVal = 0
# Output: [1,0]
 
# Constraints:
# 0 <= Number of Nodes <= 5 * 10^4
# -10^6 <= Node.val <= 10^6
# -10^6 <= insertVal <= 10^6

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode
 
        prev, curr = head, head.next
        toInsert = False

        while True:
            
            if prev.val <= insertVal <= curr.val:
                # Case #1.
                toInsert = True
            elif prev.val > curr.val:
                # Case #2. where we locate the tail element
                # 'prev' points to the tail, i.e. the largest element!
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True

            if toInsert:
                prev.next = Node(insertVal, curr)
                # mission accomplished
                return head

            prev, curr = curr, curr.next
            # loop condition
            if prev == head:
                break
        # Case #3.
        # did not insert the node in the loop
        prev.next = Node(insertVal, curr)
        return head