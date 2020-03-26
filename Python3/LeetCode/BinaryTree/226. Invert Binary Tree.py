# Invert a binary tree.

# Example:
# Input:
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Trivia:
# This problem was inspired by this original tweet by Max Howell:
# Google: 90% of our engineers use the software you wrote (Homebrew), 
# but you can’t invert a binary tree on a whiteboard so f*** off.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # M1. 递归
        if not root:
            return 
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

        # M2. 迭代
        if not root:
            return 
        q = [root]
        while q:
            cur = q.pop()
            tmp = cur.left
            cur.left = cur.right
            cur.right = tmp
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return root