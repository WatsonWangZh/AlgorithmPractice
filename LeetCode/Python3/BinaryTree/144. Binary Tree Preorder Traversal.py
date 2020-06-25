# Given a binary tree, return the preorder traversal of its nodes' values.

# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # M1. Recursion
    # def __init__(self):
    #     self.res = []

    # def preorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     if root:
    #         self.res.append(root.val)
    #         self.preorderTraversal(root.left)
    #         self.preorderTraversal(root.right)    
    #     return self.res

    # M2. Iteration with stack
    # Root Left Right 
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)

            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res
