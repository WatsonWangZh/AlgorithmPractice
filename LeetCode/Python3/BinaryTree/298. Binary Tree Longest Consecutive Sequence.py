# Given a binary tree, find the length of the longest consecutive sequence path.
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
# The longest consecutive path need to be from parent to child (cannot be the reverse).

# Example 1:
# Input:
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Output: 3
# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

# Example 2:
# Input:
#    2
#     \
#      3
#     / 
#    2    
#   / 
#  1
# Output: 2 
# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = []
        stack.append((root, 1))
        max_len = 1

        while stack:
            (n, cnt) = stack.pop()

            if n.left:
                if n.left.val == n.val + 1:
                    stack.append(((n.left, cnt+1)))
                else:
                    stack.append(((n.left, 1)))
                    
            if n.right:
                if n.right.val == n.val + 1:
                    stack.append(((n.right, cnt+1)))
                else:
                    stack.append(((n.right, 1)))

            max_len = max(max_len, cnt)
            
        return max_len