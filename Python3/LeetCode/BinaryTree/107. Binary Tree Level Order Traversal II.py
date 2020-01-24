# Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
# (ie, from left to right, level by level from leaf to root).
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # M1. 模拟
        if not root:
            return []
        q, res, tmp = [root], [], []
        cnt = 1
        while q:
            node = q.pop(0)
            tmp += [node.val]
            cnt -= 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if cnt == 0:
                cnt = len(q)
                res = [tmp] + res
                tmp = []
        return res

        # M2. 层序遍历 逆序输出
        levels, level = [], [root]
        while level and root:
            levels.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return levels[::-1]