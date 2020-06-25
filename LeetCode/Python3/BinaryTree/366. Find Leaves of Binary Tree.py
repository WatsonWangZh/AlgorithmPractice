# Given a binary tree, collect a tree's nodes as if you were doing this: 
# Collect and remove all leaves, repeat until the tree is empty.

# Example:
# Input: [1,2,3,4,5]
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Output: [[4,5,3],[2],[1]]
 
# Explanation:
# 1. Removing the leaves [4,5,3] would result in this tree:
#           1
#          / 
#         2          
# 2. Now removing the leaf [2] would result in this tree:
#           1          
# 3. Now removing the leaf [1] would result in the empty tree:
#           []         

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 递归后序遍历 以深度为标准扩充结果
        res, _ = self.helper(root)
        return res
            
    def helper(self, root):
        if not root:
            return ([], 0)
        else:
            left, l = self.helper(root.left)
            right, r = self.helper(root.right)
            
            res = []

            for i in range(min(l, r)):
                res.append(left[i] + right[i])
            if l > r:
                res.extend(left[r:])
            else:
                res.extend(right[l:])

            res.append([root.val])

            return (res, max(l, r) + 1)