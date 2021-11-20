# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #  递归 DFS
        if not root:
            return 0
        min_depth = float('inf')
        if root.left:
            min_depth = min(min_depth, self.minDepth(root.left) + 1)
        if root.right:
            min_depth = min(min_depth, self.minDepth(root.right) + 1)
        if min_depth == float('inf'):
            return 1
        return min_depth
        

        # 栈 DFS
        if not root:
            return 0
        stack, min_depth = [(root, 1),], float('inf')
        
        while stack:
            root, depth = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(min_depth, depth)
            for child in children:
                if child:
                    stack.append((child, depth + 1))
        
        return min_depth

        #  队列 BFS
        if not root:
            return 0
        node_deque = collections.deque([(root, 1),])
        
        while node_deque:
            root, depth = node_deque.popleft()
            children = [root.left, root.right]
            if not any(children):
                return depth
            for child in children:
                if child:
                    node_deque.append((child, depth + 1))
