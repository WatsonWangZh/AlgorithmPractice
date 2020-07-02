# Given the root of a binary tree, find the maximum value V for which 
# there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.
# (A node A is an ancestor of B if either: any child of A is equal to B, 
# or any child of A is an ancestor of B.)

# Example 1:
# Input: [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: 
# We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
 
# Note:
# The number of nodes in the tree is between 2 and 5000.
# Each node will have value between 0 and 100000.

# Hints:
# For each subtree, find the minimum value and maximum value of its descendants.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS O(n)
        # 一遍DFS，在DFS过程中，记录当前结点的所有父结点的最大值和最小值，
        # 然后根据当前值与前两者之间的差值更新答案。
        # 时间复杂度分析：每个结点遍历一遍O(n)。

        self.result = 0

        def dfs(root, max_v, min_v):
            if not root:
                return
            self.result =  max(self.result, abs(max_v - root.val), abs(min_v - root.val))
            max_v = max(max_v, root.val)
            min_v = min(min_v, root.val)
            dfs(root.left, max_v, min_v)
            dfs(root.right, max_v, min_v)

        dfs(root.left, root.val, root.val)
        dfs(root.right, root.val, root.val)

        return self.result
