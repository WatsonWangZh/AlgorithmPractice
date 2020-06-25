# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3

# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

     # M1.(递归) O(n)
    # 递归判断两个子树是否互为镜像。
    # 两个子树互为镜像当且仅当：
    # 两个子树的根节点值相等；
    # 第一棵子树的左子树和第二棵子树的右子树互为镜像，且第一棵子树的右子树和第二棵子树的左子树互为镜像；
    # def isSymmetric(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if not root:
    #         return True
    #     return self.helper(root.left, root.right)

    # def helper(self, root1, root2):
    #     if not root1 and not root2:
    #         return True
    #     if not root1 or not root2:
    #         return False
    #     return (root1.val == root2.val) and self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)

    # M2.(迭代) O(n)
    # 用栈模拟递归，对根节点的左子树，我们用中序遍历；对根节点的右子树，我们用反中序遍历。
    # 则两个子树互为镜像，当且仅当同时遍历两课子树时，对应节点的值相等。
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [(root, root)]
        while stack:
            node1, node2 = stack.pop()
            if node1 == None and node2 == None:
                continue
            if node1 == None or node2 == None:
                return False
            if node1.val == node2.val:
                stack.append((node1.left, node2.right))
                stack.append((node1.right, node2.left))
            else:
                return False
        return True
