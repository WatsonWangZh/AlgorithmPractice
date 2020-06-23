# Given a complete binary tree, count the number of nodes.

# Note:
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, 
# and all nodes in the last level are as far left as possible. 
# It can have between 1 and 2h nodes inclusive at the last level h.

# Example:
# Input: 
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
# Output: 6

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # M1. 不使用完美二叉树条件
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # M2. 
        hLeft, hRight = 0, 0
        pLeft, pRight = root, root

        while pLeft:
            hLeft += 1
            pLeft = pLeft.left
        
        while pRight:
            hRight += 1
            pRight = pRight.right
            
        if hLeft == hRight:
            return 2**hLeft - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# M3. Binary Search in Binary Check, BinarySeach in BinarySearch.
# https://leetcode.com/problems/count-complete-tree-nodes/solution/
class Solution:  
    def compute_depth(self, node: TreeNode) -> int:
        """
        Return tree depth in O(d) time.
        """
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists. 
        Binary search with O(d) complexity.
        """
        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None
        
    def countNodes(self, root: TreeNode) -> int:
        # if the tree is empty
        if not root:
            return 0
        
        d = self.compute_depth(root)
        # if the tree contains 1 node
        if d == 0:
            return 1
        
        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1
        
        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        return (2**d - 1) + left