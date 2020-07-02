# Given a binary tree, return the vertical order traversal of its nodes' values. 
# (ie, from top to bottom, column by column).
# If two nodes are in the same row and column, the order should be from left to right.

# Examples 1:
# Input: [3,9,20,null,null,15,7]
#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7 
# Output:
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]

# Examples 2:
# Input: [3,9,8,4,0,1,7]
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7 
# Output:
# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]

# Examples 3:
# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2
# Output:
# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
# ]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # https://www.cnblogs.com/grandyang/p/5278930.html
        # 这道题让我们竖直遍历二叉树，并把每一列存入一个二维数组，我们看题目中给的第一个例子，
        # 3和15属于同一列，3在前，第二个例子中，3,5,2在同一列，3在前，5和2紧随其后，
        # 那么我们隐约的可以感觉到好像是一种层序遍历的前后顺序，那么我们如何来确定列的顺序呢，
        # 我们可以把根节点给个序号0，然后开始层序遍历，凡是左子节点则序号减1，右子节点序号加1，
        # 这样我们可以通过序号来把相同列的节点值放到一起。
        # 然后遍历返回结果即可。
        
        # 层序遍历 横向排序
        q = [(root, 0)]
        h = defaultdict(list)
        while q:
            p = []
            for node, key in q:
                if node:
                    # if no ',' , Raise TypeError: 'int' object is not iterable 
                    h[key] += node.val,
                    p += (node.left, key-1), (node.right, key + 1)
            q = p

        res = []
        for key in list(sorted(h.keys())):
            # if no ',' , Raise TypeError: 'int' object is not iterable 
            res += h[key],

        return res