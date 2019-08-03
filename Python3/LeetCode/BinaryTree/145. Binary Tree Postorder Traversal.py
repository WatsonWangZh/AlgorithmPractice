# Given a binary tree, return the postorder traversal of its nodes' values.
# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output: [3,2,1]
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
        
    # def postorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     if root:
    #         self.postorderTraversal(root.left)
    #         self.postorderTraversal(root.right)
    #         self.res.append(root.val)
    #     return self.res

    # M2. Iteration 
    # Root Right Left , then reverse it
    def postorderTraversal(self, root):
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

            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]    
