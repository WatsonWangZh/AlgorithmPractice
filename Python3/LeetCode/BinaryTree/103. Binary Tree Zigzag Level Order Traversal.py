# Given a binary tree, return the zigzag level order traversal of its nodes' values. 
# (ie, from left to right, then right to left for the next level and alternate between).
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BFS 模拟 分奇偶
        res = []
        if not root:
            return res
        mark = True
        level = [root]
        while level:
            if mark:
                res.append([ele.val for ele in level])
            else:
                res.append([ele.val for ele in level[::-1]])
            mark = not mark
            nextLevel = []
            for ele in level:
                if ele.left:
                    nextLevel.append(ele.left)
                if ele.right:
                    nextLevel.append(ele.right)
            level = nextLevel
        return res