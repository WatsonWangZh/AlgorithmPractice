# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as 
# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:
# Given the sorted array: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 递归中序遍历 O(n)
        # Inorder Traversal: Always Choose Left Middle Node as a Root
        return self.BST_helper(nums, 0, len(nums)-1)
    
    def BST_helper(self, nums, left, right):
        if left > right:
            return None
        if left == right:
            return TreeNode(nums[left])
        else:
            middle = left + right >> 1
            node = TreeNode(nums[middle])
            node.left = self.BST_helper(nums, left, middle-1)
            node.right = self.BST_helper(nums, middle+1, right)
            return node