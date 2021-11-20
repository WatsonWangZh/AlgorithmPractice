# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical 
# and the nodes have the same value.

# Example 1:
# Input:     1         1
#           / \       / \
#          2   3     2   3
#         [1,2,3],   [1,2,3]
# Output: true

# Example 2:
# Input:     1         1
#           /           \
#          2             2
#         [1,2],     [1,null,2]
# Output: false

# Example 3:
# Input:     1         1
#           / \       / \
#          2   1     1   2
#         [1,2,1],   [1,1,2]
# Output: false

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 递归 O(n)
        # 递归判断：两个二叉树相等，当且仅当根节点的值相等，且左右两个子树分别相等。
        # 时间复杂度分析：两棵二叉树分别遍历一遍，所以时间复杂度是 O(n)。
        if q is None and p is None:
            return True
        elif q is None or p is None:
            return False
        else:
            return q.val== p.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
