# Given a binary tree, each node has value 0 or 1.  
# Each root-to-leaf path represents a binary number 
# starting with the most significant bit.  
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, 
# then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers 
# represented by the path from the root to that leaf.
# Return the sum of these numbers.

# Example 1:
#      _1_
#     /   \
#    0     1
#   / \   / \
#  0   1 0   1
# Input: [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

# Note:
# The number of nodes in the tree is between 1 and 1000.
# node.val is 0 or 1.
# The answer will not exceed 2^31 - 1.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 深度优先搜索 O(n)
        # 深度优先搜索的时候用一个参数记录父节点的二进制值，
        # 那么当前结点到根的二进制值就是父结点乘以2加上当前结点的值。
        # 如果遍历到叶子结点，那么就更新答案。
        # 时间复杂度分析：每个结点遍历一次，所以时间复杂度为O(n)。
        self.ans = 0
        self.mod = 10 ** 9 + 7

        def dfs(r, temp_sum):
            temp_sum = temp_sum * 2 + r.val
            if r.left == None and r.right == None:
                self.ans += temp_sum
                return
            if r.left:
                dfs(r.left, temp_sum)
            if r.right:
                dfs(r.right, temp_sum)

        dfs(root, 0)
        return self.ans % self.mod

        