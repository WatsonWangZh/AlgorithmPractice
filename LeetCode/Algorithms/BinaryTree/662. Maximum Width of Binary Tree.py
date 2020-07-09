# Given a binary tree, write a function to get the maximum width of the given tree. 
# The width of a tree is the maximum width among all levels. 
# The binary tree has the same structure as a full binary tree, but some nodes are null.
# The width of one level is defined as the length between the end-nodes 
# (the leftmost and right most non-null nodes in the level, 
# where the null nodes between the end-nodes are also counted into the length calculation.

# Example 1:
# Input: 
#            1
#          /   \
#         3     2
#        / \     \  
#       5   3     9 
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

# Example 2:
# Input: 
#           1
#          /  
#         3    
#        / \       
#       5   3     
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).

# Example 3:
# Input: 
#           1
#          / \
#         3   2 
#        /        
#       5      
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).

# Example 4:
# Input: 
#           1
#          / \
#         3   2
#        /     \  
#       5       9 
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# M1. BFS 记录每一层所有元素
# 用本层最后元素的下标减去当前层第一个元素的下标，即为结果。
from collection import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 1
        # q = deque((root, 0))  # q:[root, 0]
        q = deque() 
        # The key to solve the problem though lie on how we index the nodes that are on the same level.
        q.append((root, 0)) # q:[(root, 0)]

        while q:
            level_length = len(q)
            _, level_head_index = q[0]
            for _ in range(level_length):
                node, col_index = q.popleft()
                if node.left:
                    q.append([node.left, 2*col_index])
                if node.right:
                    q.append([node.right, 2*col_index+1])
            res = max(res, col_index-level_head_index+1)

        return res

# M2. DFS 只记录当前层leftmost节点的下标值
# 在遍历过程中更新宽度值。
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        # table contains the first col_index for each level
        first_col_index_table = {}
        res = 0

        def DFS(node, depth, col_index):
            nonlocal res
            if node is None:
                return
            # if the entry is empty, set the value
            if depth not in first_col_index_table:
                first_col_index_table[depth] = col_index

            res = max(res, col_index - first_col_index_table[depth] + 1)

            # Preorder DFS, with the priority on the left child
            # The key to solve the problem though lie on how we index the nodes that are on the same level.
            DFS(node.left, depth+1, 2*col_index)
            DFS(node.right, depth+1, 2*col_index + 1)

        DFS(root, 0, 0)

        return res