# Given two non-empty binary trees s and t, 
# check whether tree t has exactly the same structure and node values with a subtree of s. 
# A subtree of s is a tree consists of a node in s and all of this node's descendants. 
# The tree s could also be considered as a subtree of itself.

# Example 1:
# Given tree s:
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4 
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.

# Example 2:
# Given tree s:
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2

# Hints:
# Which approach is better here- recursive or iterative?
# If recursive approach is better, can you write recursive function with its parameters?
# Two trees s and t are said to be identical if their root values are same 
# and their left and right subtrees are identical. Can you write this in form of recursive formulae?
# Recursive formulae can be: 
# isIdentical(s,t)= s.val==t.val AND isIdentical(s.left,t.left) AND isIdentical(s.right,t.right)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # M1. 递归先序遍历
        # print(self.preorder(s),len(self.preorder(s)))
        # print(self.preorder(t),len(self.preorder(t)))
        return self.preorder(t) in self.preorder(s)
        
    def preorder(self, root): 
        if not root:
            return "*"
        else:
            # “ ” for case like [12] and [2]
            # You can also note that we've added a '#' before every considering every value. 
            # If this isn't done, the trees of the form s:[23, 4, 5] and t:[3, 4, 5] will also give a true result 
            # since the preorder string of the t("23 4 lnull rull 5 lnull rnull") will be a substring of the preorder string of s("3 4 lnull rull 5 lnull rnull"). 
            # Adding a '#' before the node's value solves this problem.
            return " " + str(root.val) + self.preorder(root.left) + self.preorder(root.right)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # M2. 模拟比较
        # for case middle 
        if not s or not t:
            return False

        isIdentical = False
        if s.val == t.val:
            isIdentical = self.tree_comparor(s,t)

        if isIdentical:
            return True
        else:
            return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    
    def tree_comparor(self, t1, t2):
        if t1 is None or t2 is None:
            if t1 is None and t2 is None:
                return True
            else:
                return False

        if t1.val != t2.val:
            return False
        else:
            return self.tree_comparor(t1.left,t2.left) and self.tree_comparor(t1.right,t2.right)