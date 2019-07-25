# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:
#     2
#    / \
#   1   3
# Input: [2,1,3]
# Output: true

# Example 2:
#     5
#    / \
#   1   4
#      / \
#     3   6
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # M1.DFS
    # 从上到下判断，在往下遍历子树的过程中，根据父节点的信息记录并更新子树的值的大小范围
    # 如果当前结点超过了当前的大小范围，则返回false
    # 否则递归遍历左子树，将左子树的最大值的范围更新为当前结点的值；
    # 递归遍历右子树，将右子树的最小值的范围更新为当前结点的值。

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, float('-inf'), float('inf'))

    def dfs(self, node, lower_bound, upper_bound):
        if not node: 
            return True
        if node.val >= upper_bound or node.val <= lower_bound:
            return False
        left = self.dfs(node.left, lower_bound, node.val)
        right = self.dfs(node.right, node.val, upper_bound)
        return left and right

    # M2.中序遍历，看是否严格递增
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = []
        self.inOrder(root, nodes)
        for i in range(len(nodes) - 1):
            if nodes[i] >= nodes[i+1]:
                return False
        return True

    def inOrder(self, root, nodes):
        if not root:
            return 
        self.inOrder(root.left, nodes)
        nodes.append(root.val)
        self.inOrder(root.right, nodes)
        