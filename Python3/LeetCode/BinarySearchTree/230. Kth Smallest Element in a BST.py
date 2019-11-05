# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Example 1:
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1

# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3

# Follow up:
# What if the BST is modified (insert/delete operations) often 
# and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# Hints:
# Try to utilize the property of a BST.
# Try in-order traversal. (Credits to @chan13)
# What if you could modify the BST node's structure?
# The optimal runtime complexity is O(height of BST).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # M1. 递归 O(n)
        # 中序遍历规则遍历整棵BST，并用数组记录结点的遍历顺序,输出第 k 个结点即可。

        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    
        return inorder(root)[k - 1]

        # M2. 栈迭代 O(lgn+k)
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right