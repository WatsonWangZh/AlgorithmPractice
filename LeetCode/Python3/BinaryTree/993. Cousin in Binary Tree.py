# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
# We are given the root of a binary tree with unique values, 
# and the values x and y of two different nodes in the tree.
# Return true if and only if the nodes corresponding to the values x and y are cousins.

# Example 1:
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false

# Example 2:
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true

# Example 3:
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
 
# Note:
# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # M1. DFS
        self.m = collections.defaultdict(tuple)
        self.dfs(root, None, 0)
        px, dx = self.m[x]
        py, dy = self.m[y]
        return dx == dy and px != py
    
    def dfs(self, root, parent, depth):
        if not root: return
        self.m[root.val] = (parent, depth)
        self.dfs(root.left, root, depth + 1)
        self.dfs(root.right, root, depth + 1)


import collections
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # M2. BFS
        m = collections.defaultdict(tuple)
        q = collections.deque()
        q.append((root, None))
        depth = 0
        while q:
            size = len(q)
            for i in range(size):
                node, p = q.popleft()
                if not node: continue
                m[node.val] = (p, depth)
                q.append((node.left, node))
                q.append((node.right, node))
            depth += 1
        px, dx = m[x]
        py, dy = m[y]
        return dx == dy and px != py
