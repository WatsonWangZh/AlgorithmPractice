# Given an integer n, 
# generate all structurally unique BST's (binary search trees) that store values 1 ... n.

# Example:
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # DFS O(Cn2n/(n+1))
        # 递归搜索所有方案。
        # 对于每段连续的序列 l,l+1,…r，枚举二叉搜索树根节点的位置；
        # 分别递归求出左右子树的所有方案；
        # 左子树的任意一种方案和右子树的任意一种方案拼在一起，可以得到当前节点的一种方案，
        # 所以我们将左右子树的所有方案两两组合，并记录在答案中。
        # 时间复杂度分析：我们来求一下当节点数是 n 时，总共有多少种方案。假设方案数是 hn，则有 hn=∑n−1k=0hk∗hn−1−k。
        # 所以 hn 是卡特兰数，其通项公式是 hn=Cn2n/(n+1)。所以时间复杂度是 O(Cn2n/(n+1))。

        if n == 0:
            return []
        memo = {}
        return self.helper(memo, 1, n)

    def helper(self, memo, start, end):
        if (start, end) in memo:
            return memo[(start, end)]
        elif start == end:
            memo[(start, end)] = [TreeNode(start)]
            return memo[(start, end)]
        elif start > end:
            return [None]
        
        
        result = []
        for root in range(start, end+1):
            possible_left = self.helper(memo, start, root-1)
            possible_right = self.helper(memo, root+1, end)
            for left in possible_left:
                for right in possible_right:
                    root_node = TreeNode(root)
                    root_node.left = left
                    root_node.right = right
                    result.append(root_node)
                    
        memo[(start, end)] = result
        
        return result
    