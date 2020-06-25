# The thief has found himself a new place for his thievery again. 
# There is only one entrance to this area, called the "root." 
# Besides the root, each house has one and only one parent house. 
# After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
# It will automatically contact the police if two directly-linked houses 
# were broken into on the same night.
# Determine the maximum amount of money the thief can rob tonight without alerting the police.

# Example 1:
# Input: [3,2,3,null,3,null,1]
#      3
#     / \
#    2   3
#     \   \ 
#      3   1
# Output: 7 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

# Example 2:
# Input: [3,4,5,1,3,null,1]
#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # 树形动规DP O(n)
    # 典型的树形DP问题。
    # 状态表示：
        # f[i][0]表示已经偷完以 i 为根的子树，且不在 i 行窃的最大收益；
        # f[i][1]表示已经偷完以 i 为根的子树，且在 i 行窃的最大收益；
    # 状态转移：
        # f[i][1]：因为在 i 行窃，所以在 i 的子节点不能行窃，只能从f[i->left][0]和f[i->right][0]转移；
        # f[i][0]：因为不在 i 行窃，所以对 i 的子节点没有限制，直接用左右子节点的最大收益转移即可；
    # 时间复杂度分析：总共有 n 个状态，每个状态进行转移的计算量是 O(1)。所以总时间复杂度是 O(n)。

    # M2. 优化
    def __init__(self):
        self.profit = {}
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return [0, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            res = [0, 0]
            res[0] = max(left[1], left[0]) + max(right[1], right[0])
            res[1] = root.val + left[0] + right[0]
            return res
        return max(dfs(root)[0], dfs(root)[1])

    # M1. Easy to Understand but TLE
    # def rob(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if not root:
    #         return 0
    #     self.ans = 0
    #     self.rob_node(root, 1)
    #     #print(self.ans)
    #     self.rob_node(root, 0)    
    #     #print(self.ans)
    #     return self.ans
    
    # def rob_node(self, n, is_steal):
    #     if not n:
    #         return 0
    #     if is_steal:
    #         ans = n.val + self.rob_node(n.left, 0) + self.rob_node(n.right, 0)
    #     else:
    #         l0, l1 = self.rob_node(n.left, 0), self.rob_node(n.left, 1) 
    #         r0, r1 = self.rob_node(n.right, 0), self.rob_node(n.right, 1) 
    #         ans = max(l0 + r0, l0 + r1, l1 + r0, l1 + r1)

    #     self.ans = max(self.ans, ans)
    #     return ans
