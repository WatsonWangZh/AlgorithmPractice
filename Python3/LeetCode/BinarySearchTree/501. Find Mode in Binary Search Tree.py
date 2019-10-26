# Given a binary search tree (BST) with duplicates, 
# find all the mode(s) (the most frequently occurred element) in the given BST.
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# For example:
# Given BST [1,null,2,2],
#    1
#     \
#      2
#     /
#    2
# return [2].

# Note: If a tree has more than one mode, you can return them in any order.
# Follow up: Could you do that without using any extra space? 
# (Assume that the implicit stack space incurred due to recursion does not count).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 中序遍历 查相邻 O(n)
        p = root
        stack = []
        res = []

        val, count = 0, 0
        cur_max = 0

        while p or stack:
            while p:
                stack.append(p)
                p = p.left

            p = stack.pop()
            if p.val == val:
                count += 1
            else:
                val = p.val
                count = 1

            if count == cur_max:
                res.append(p.val)
            elif count > cur_max:
                res = [p.val]
                cur_max = count

            p = p.right
        return res