# Given a Binary Search Tree and a target number, return true if there exist two elements 
# in the BST such that their sum is equal to the given target.
# Example 1:
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# Target = 9
# Output: True
 
# Example 2:
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# Target = 28
# Output: False

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.node_val_list = []

    def inorder(self, root):
        if not root:
            return None
        self.inorder(root.left)
        self.node_val_list.append(root.val)
        self.inorder(root.right)
        return self.node_val_list

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # 通过中序遍历生成一个排序的数组, 然后通过排序的数组，来做选择。
        sorted_array = self.inorder(root)
        left = 0
        right = len(sorted_array)-1
        while left < right:
            if sorted_array[left] + sorted_array[right] == k:
                return True
            elif sorted_array[left] + sorted_array[right] < k:
                left += 1
            else:
                right -= 1
        return False
