# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from 
# the root node down to the farthest leaf node.
# Note: A leaf is a node with no children.

# Example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 递归 O(n)
    # 递归求解：
    # 当前树的最大深度等于左右子树的最大深度加1。
    # 时间复杂度分析：树中每个节点只被遍历一次，所以时间复杂度是 O(n)。
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
