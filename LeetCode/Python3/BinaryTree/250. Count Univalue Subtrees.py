# Given a binary tree, count the number of uni-value subtrees.
# A Uni-value subtree means all nodes of the subtree have the same value.

# Example :
# Input:  root = [5,1,5,5,5,null,5]
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
# Output: 4

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # https://www.youtube.com/watch?v=gnSuBULGasw
        # 自底向上递归 O(lgn)

        def helper(root):
            if root is None:
                return True
            left = helper(root.left)
            right = helper(root.right)

            if root.left and root.right:
                if left and right and root.val == root.left.val and root.val == root.right.val:
                    self.result += 1
                    return True
                else:
                    return False

            elif root.left:
                if left and root.val == root.left.val:
                    self.result += 1
                    return True
                else:
                    return False

            elif root.right:
                if right and root.val == root.right.val:
                    self.result += 1
                    return True
                else:
                    return False

            else:
                self.result += 1
                return True

        self.result = 0
        helper(root)
        return self.result