# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.
# Note: A leaf is a node with no children.

# Example:
# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.

# Example 2:
# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS模拟
        if not root:
            return 0
        return self.helper(root, 0)
    
    def helper(self, root, cur_val):
        if not root:
            return 0
        if not root.left and not root.right:
            return cur_val * 10 + root.val
        return self.helper(root.left, cur_val*10 + root.val) + self.helper(root.right, cur_val*10 + root.val)

# 迭代求解 O(n) O(lgn)
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, 0) ]
        
        while stack:
            root, curr_number = stack.pop()
            if root:
                curr_number = curr_number * 10 + root.val
                # if it's a leaf, update root-to-leaf sum
                if root.left is None and root.right is None:
                    res += curr_number
                else:
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))
                        
        return res


# 先序递归 O(n) O(lgn)
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        
        def preorder(root, curr_number):
            nonlocal res
            if root:
                curr_number = curr_number * 10 + root.val
                
                # if it's a leaf, update root-to-leaf sum
                if not root.left and not root.right:
                    res += curr_number
                    
                preorder(root.left, curr_number)
                preorder(root.right, curr_number)
                
        preorder(root, 0)
        return res
    
# Awesome Morris Preorder Traversal! O(n) O(1)
class Solution:
    def sumNumbers(self, root: TreeNode):
        root_to_leaf = curr_number = 0
        
        while root:  
            # If there is a left child,
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left: 
                # Predecessor node is one step to the left 
                # and then to the right till you can.
                predecessor = root.left 
                steps = 1
                while predecessor.right and predecessor.right is not root: 
                    predecessor = predecessor.right 
                    steps += 1

                # Set link predecessor.right = root
                # and go to explore the left subtree
                if predecessor.right is None:
                    curr_number = curr_number * 10 + root.val                    
                    predecessor.right = root  
                    root = root.left  
                # Break the link predecessor.right = root
                # Once the link is broken, 
                # it's time to change subtree and go to the right
                else:
                    # If you're on the leaf, update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # This part of tree is explored, backtrack
                    for _ in range(steps):
                        curr_number //= 10
                    predecessor.right = None
                    root = root.right 
                    
            # If there is no left child
            # then just go right.        
            else: 
                curr_number = curr_number * 10 + root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right
                        
        return root_to_leaf