# Given a non-empty binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes 
# from some starting node to any node in the tree along the parent-child connections. 
# The path must contain at least one node and does not need to go through the root.

# Example 1:
# Input: [1,2,3]
#        1
#       / \
#      2   3
# Output: 6

# Example 2:
# Input: [-10,9,20,null,null,15,7]
#    -10
#    / \
#   9  20
#     /  \
#    15   7
# Output: 42

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sums = []
        
        def dfs(root):
            if root.left and root.right:
                left = dfs(root.left)
                right = dfs(root.right)
                sums.append(root.val + left)
                sums.append(root.val + right)
                sums.append(root.val + left + right)
                sums.append(root.val)
                return max(root.val, root.val + left, root.val + right)
            elif root.left:
                left = dfs(root.left)
                sums.append(root.val + left)
                sums.append(root.val)
                return max(root.val, root.val + left)
            elif root.right:
                right = dfs(root.right)
                sums.append(root.val + right)
                sums.append(root.val)
                return max(root.val, root.val + right)
            else:
                sums.append(root.val)
                return root.val
        dfs(root)
        return max(sums)
        