# Given a binary tree, find the leftmost value in the last row of the tree.

# Example 1:
# Input:
#     2
#    / \
#   1   3
# Output:
# 1

# Example 2:
# Input:
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
# Output:
# 7
# Note: You may assume the tree (i.e., the given root node) is not NULL.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 模拟层序遍历 O(n)
        if not root:
            return None
        q = deque([root])
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if i == 0:
                    leftmost = cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return leftmost