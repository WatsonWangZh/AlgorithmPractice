# Given a binary tree, you need to compute the length of the diameter of the tree. 
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
# This path may or may not pass through the root.
# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 递归遍历 O(n)
    # 递归函数的返回值定义为从当前结点到叶子结点的最大长度，当前结点为空返回 -1。
    # 递归时，分别得到左右子树递归的返回值，则可以更新答案 ans = max(ans, d1 + d2 + 2)；
    # 然后返回 max(d1, d2) + 1
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxL = 0
        
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            self.maxL = max(self.maxL, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.maxL
