# Return the root node of a binary search tree that matches the given preorder traversal.
# (Recall that a binary search tree is a binary tree where for every node, 
# any descendant of node.left has a value < node.val, 
# and any descendant of node.right has a value > node.val.  
# Also recall that a preorder traversal displays the value of the node first, 
# then traverses node.left, then traverses node.right.)
# It's guaranteed that for the given test cases 
# there is always possible to find a binary search tree with the given requirements.

# Example 1:
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

# Constraints:
# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 10^8
# The values of preorder are distinct.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        if not preorder: return None
        root = TreeNode(preorder[0])
        N = len(preorder)
        i = 1
        while i < N:
            if preorder[i] > preorder[0]:
                break
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
