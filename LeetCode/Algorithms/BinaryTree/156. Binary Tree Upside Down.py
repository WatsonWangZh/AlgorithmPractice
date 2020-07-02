# Given a binary tree where all the right nodes are either leaf nodes with a sibling 
# (a left node that shares the same parent node) or empty, 
# flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. 
# Return the new root.
# Example:
# Input: [1,2,3,4,5]
#     1
#    / \
#   2   3
#  / \
# 4   5
# Output: return the root of the binary tree [4,5,2,#,#,3,1]
#    4
#   / \
#  5   2
#     / \
#    3   1  
# Clarification:
# Confused what [4,5,2,#,#,3,1] means? Read more below on how binary tree is serialized on OJ.
# The serialization of a binary tree follows a level order traversal, 
# where '#' signifies a path terminator where no node exists below.
# Here's an example:
#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
# The above binary tree is serialized as [1,2,3,#,#,4,#,#,5].

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 栈模拟 O(n)
        # 时间复杂度分析：
        # 每个节点仅被遍历一遍，所以时间复杂度是 O(n)。
        
        if not root:
            return None
        
        stack = []
        node = root
        
        while node:
            stack.append(node)
            node = node.left
            
        root = TreeNode(stack.pop(-1).val)
        curr = root
        while stack:
            node = stack.pop(-1)
            curr.left = node.right
            curr.right = TreeNode(node.val)
            curr = curr.right
        
        return root