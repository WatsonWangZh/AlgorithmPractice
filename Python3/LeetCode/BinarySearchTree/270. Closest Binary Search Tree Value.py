# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Note:
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.

# Example:
# Input: root = [4,2,5,1,3], target = 3.714286
#     4
#    / \
#   2   5
#  / \
# 1   3
# Output: 4

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        # M1. 中序遍历，线性查找 O(n) 

        # def inorder(root):
        #     return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        
        # return min(inorder(root), key = lambda x: abs(target - x))

        # M2. 二分查找 O(lgn)

        def traverse(root, target):
            if root is None:
                return
            if (abs(root.val-target) < self.difference):
                self.difference = abs(root.val - target)
                self.result = root.val
            if target <= root.val:
                traverse(root.left, target)
            else:
                traverse(root.right, target)

        self.result = 0
        self.difference = sys.maxsize

        traverse(root, target)

        return self.result