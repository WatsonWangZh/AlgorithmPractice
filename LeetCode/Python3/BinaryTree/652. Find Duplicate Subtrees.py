# Given a binary tree, return all duplicate subtrees. 
# For each kind of duplicate subtrees, 
# you only need to return the root node of any one of them.
# Two trees are duplicate if they have the same structure with same node values.

# Example 1:
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# The following are two duplicate subtrees:
#       2
#      /
#     4
# and
#     4
# Therefore, you need to return above trees' root in the form of a list.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        # 深度优先遍历，哈希表 O(n)
        # 记录每个子树经过哈希后的数量，哈希方法可以用最简单的前序遍历，
        # 即 根,左子树,右子树 的方式递归构造。
        # 逗号和每个叶子结点下的空结点的位置需要保留。
        # 若发现当前子树在哈希表第二次出现，则将该结点记入答案列表。
        # 时间复杂度
        # 每个结点仅遍历一次，单次操作的时间复杂度为 O(1)，故总时间复杂度为 O(n)。

        count_dict = collections.Counter()
        result = []
        
        def dfs(node):
            if not node:
                return "#"
            path = "{},{},{}".format(node.val, dfs(node.left), dfs(node.right))
            count_dict[path] += 1
            if count_dict[path] == 2:
                result.append(node)
            return path 
        
        dfs(root)
        return result