# Given a non-empty binary search tree and a target value, 
# find k values in the BST that are closest to the target.

# Note:
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

# Example:
# Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
#     4
#    / \
#   2   5
#  / \
# 1   3
# Output: [4,3]

# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

# Hints:
# Consider implement these two helper functions:
# getPredecessor(N), which returns the next smaller node to N.
# getSuccessor(N), which returns the next larger node to N.
# Try to assume that each node has a parent pointer, it makes the problem much easier.
# Without parent pointer we just need to keep track of the path from the root to the current node using a stack.
# You would need two stacks to track the path in finding predecessor and successor node separately.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # 中序遍历，遍历中更新结果
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)

            if len(res) == k:
                if abs(root.val - target) < abs(res[0] - target):
                    res.pop(0)
                else:
                    return
            res.append(root.val)

            inorder(root.right)
            
        res = []
        inorder(root)
        return res