# Given a binary search tree with non-negative values, 
# find the minimum absolute difference between values of any two nodes.

# Example:
# Input:
#    1
#     \
#      3
#     /
#    2
# Output:
# 1
# Explanation:
# The minimum absolute difference is 1, 
# which is the difference between 2 and 1 (or between 2 and 3).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 二叉搜索树的最小绝对差
    # 由于BST的左<根<右，中序遍历结果即为有序，转化为在有序树组中求最小差值
    def getMinimumDifference(self, root: TreeNode) -> int:
        ret = []
        self.helper(ret, root)
        m = ret[-1] - ret[0]
        last = None
        for i in ret:
            if last is None:
                last = i
            else:
                if m is None or i - last < m:
                    m = i - last
                last = i
        return m
                
        
    def helper(self, ret, root):
        if root:
            self.helper(ret, root.left)
            ret.append(root.val)
            self.helper(ret, root.right)
