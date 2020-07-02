# Given a binary tree, flatten it to a linked list in-place.
# For example, given the following tree:
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
# Hints:
# If you notice carefully in the flattened tree, 
# each node's right child points to the next node of a pre-order traversal.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # https://www.cnblogs.com/grandyang/p/4293853.html
        # M1. 递归之一
        if not root:
            return 
        if root.left:
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)
            
        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp

        # M2. 迭代 
        if not root:
            return None
        s = [root]
        while s:
            cur = s.pop()
            if cur.left:
                p = cur.left
                while p.right:
                    p = p.right
                p.right = cur.right
                cur.right = cur.left
                cur.left = None
            if cur.right:
                s.append(cur.right)

        # M3. 非迭代
        cur = root
        while cur:
            if cur.left:
                p = cur.left
                while p.right:
                    p = p.right
                p.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
        
