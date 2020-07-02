# Given a binary tree, find the length of the longest path 
# where each node in the path has the same value. 
# This path may or may not pass through the root.
# The length of path between two nodes 
# is represented by the number of edges between them.

# Example 1:
# Input:

#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output: 2

# Example 2:
# Input:
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output: 2

# Note: The given binary tree has not more than 10000 nodes. 
# The height of the tree is not more than 1000.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longestPath = 0

        def helper(node):
            if not node or (not node.left and not node.right):
                return 0

            leftp = helper(node.left)
            rightp = helper(node.right)
            
            if node.left and node.right and node.left.val == node.right.val == node.val:
                self.longestPath = max(self.longestPath, leftp + rightp + 2)
                return max(leftp, rightp) + 1
            
            if node.left and node.val == node.left.val:
                self.longestPath = max(self.longestPath, leftp + 1)
                return leftp + 1
            
            if node.right and node.val == node.right.val:
                self.longestPath = max(self.longestPath, rightp + 1)
                return rightp + 1
            return 0
            
        helper(root)
        return self.longestPath
