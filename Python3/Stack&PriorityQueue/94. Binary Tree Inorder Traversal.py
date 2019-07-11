# Given a binary tree, return the inorder traversal of its nodes' values.
# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 中序遍历 M1.递归实现 M2.栈实现
    
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     # M1.递归实现
    #     res = []
    #     self.helper(root, res)
    #     return res

    # def helper(self, root, res):
    #     if root is None:
    #         return
    #     self.helper(root.left)
    #     res.append(root.val)
    #     self.helper(root.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # M2.栈实现
        stack, res = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                res.append(tmpNode.val)
                root = tmpNode.right
        return res
