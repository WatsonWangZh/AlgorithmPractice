# Find the sum of all left leaves in a given binary tree.

# Example:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # An empty root is one of the test cases!
        if not root:
            return 0

        def process_subtree(subtree, is_left):
            
            # Base case: This is a leaf node.
            if subtree and not subtree.left and not subtree.right:
                return subtree.val if is_left else 0
            
            # Recursive case: We need to add and return the results of the 
            # left and right subtrees.
            res = 0
            if subtree.left:
                res += process_subtree(subtree.left, True)
            if subtree.right:
                res += process_subtree(subtree.right, False)
                
            return res
        
        # Call the recursive function on the root node to start the process.
        # We need to be careful of the case that the root is empty.
        return process_subtree(root, False)
