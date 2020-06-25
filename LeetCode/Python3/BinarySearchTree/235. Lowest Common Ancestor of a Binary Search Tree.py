# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes p and q 
# as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”

# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
#          ______6______
#        /              \
#     __2__           ___8__
#    /      \        /      \
#   0       _4_     7        9
#          /   \
#         3     5

# Example 1:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Example 2:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, 
# since a node can be a descendant of itself according to the LCA definition.
 
# Note:
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 暴力 O(h) h为树的高度
    # 由于这是一棵二叉查找树，我们可以利用二叉查找树的性质来从根结点开始寻找。
    # 首先根结点必定是候选公共祖先，接着如果 p 和 q 同时出现在左子树，则我们往左儿子移动；
    # 如果 p 和 q同时出现在右子树，则我们往右儿子移动；
    # 若发现不满足 2 中的两个条件，则停止寻找，当前结点就是最近公共祖先。
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (p.val-root.val) * (q.val-root.val) <= 0:
            return root
        elif p.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)
            