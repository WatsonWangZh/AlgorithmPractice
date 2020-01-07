# Given a binary tree and a sum, 
# determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# Note: A leaf is a node with no children.
# Example:
# Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # 简单递归
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        if root.left and self.hasPathSum(root.left, sum-root.val):
            return True
        if root.right and self.hasPathSum(root.right, sum-root.val):
            return True