# Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), 
# where largest means subtree with largest number of nodes in it.
# Note:
# A subtree must include all of its descendants.

# Example:
# Input: [10,5,15,1,8,null,7]
#    10 
#    / \ 
#   5  15 
#  / \   \ 
# 1   8   7
# Output: 3
# Explanation: The Largest BST Subtree in this case is the highlighted one.
#              The return value is the subtree's size, which is 3.

# Follow up:
# Can you figure out ways to solve it with O(n) time complexity?

# Hints:
# You can recursively use algorithm similar to 98. Validate Binary Search Tree at each node of the tree, 
# which will result in O(nlogn) time complexity.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # https://www.youtube.com/watch?v=4fiDs7CCxkc
        # 自底向上 Bottom Up
        def determineBST(root):
            # Edge Case
            if not root.left and not root.right:
                self.max_node = max(self.max_node, 1)
                return True, 1, root.val, root.val
            
            if root.left:
                left_is_bst,  l_cnt, l_max, l_min = determineBST(root.left)
            else:
                left_is_bst,  l_cnt, l_max, l_min = True, 0, root.val, root.val
            if root.right:
                right_is_bst, r_cnt, r_max, r_min = determineBST(root.right)
            else:
                right_is_bst, r_cnt, r_max, r_min = True, 0, root.val, root.val
            
            # Merge for the bigger BST and update max_node cnt and temp_node cnt
            if left_is_bst and right_is_bst and (not root.left or l_max < root.val) and (not root.right or r_min > root.val):
                self.max_node = max(self.max_node, l_cnt+r_cnt+1)
                return True, l_cnt+r_cnt+1, r_max, l_min
            else:
                return False, 0, 0, 0
            
        if not root:
            return 0
        self.max_node = 0

        determineBST(root)

        return self.max_node