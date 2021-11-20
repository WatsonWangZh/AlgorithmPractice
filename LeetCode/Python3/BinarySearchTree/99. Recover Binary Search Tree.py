# Two elements of a binary search tree (BST) are swapped by mistake.
# Recover the tree without changing its structure.

# Example 1:
# Input: [1,3,null,null,2]
#    1
#   /
#  3
#   \
#    2
# Output: [3,1,null,null,2]
#    3
#   /
#  1
#   \
#    2

# Example 2:
# Input: [3,1,4,null,null,2]
#   3
#  / \
# 1   4
#    /
#   2
# Output: [2,1,4,null,null,3]
#   2
#  / \
# 1   4
#    /
#   3
# Follow up:
# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 思路: 分成两步 1.得出中序遍历结果 2.在中序遍历结果中找到被交换值的结点，然后交换其值
        # Morris-traversal O(n)
        # 这道题目如果用递归做，递归的层数最坏是 O(n)O(n) 级别的，所以系统栈的空间复杂度是 O(n)，
        # 与题目要求的 O(1)O(1) 额外空间不符。
        # 同理用栈模拟递归的迭代方式的空间复杂度也是 O(n)O(n)，不符合题目要求。
        # 这道题目可以用Morris-traversal算法，该算法可以用额外 O(1) 的空间，以及 O(n) 的时间复杂度，
        # 中序遍历一棵二叉树。

        first, second, pre = None, None, None
        cur = root
        while cur:
            if not cur.left:
                #visit cur
                if pre and pre.val > cur.val:
                    if not first:
                        first = pre
                    second = cur
                pre = cur
                #end visit cur
                cur = cur.right
            else:
                p = cur.left #predecessor 
                while p.right and p.right != cur:
                    p = p.right
                if not p.right:
                    p.right = cur
                    cur = cur.left
                else:
                    p.right = None
                    if pre and pre.val > cur.val:
                        if not first:
                            first = pre
                        second = cur
                    pre = cur
                    cur = cur.right

        if first and second:
            first.val, second.val = second.val, first.val
        