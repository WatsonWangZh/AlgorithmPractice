# Given a binary tree, return the level order traversal of its nodes' values. 
# (ie, from left to right, level by level).
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


# 二刷
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # BFS O(n)
        # 宽度优先遍历，一层一层来做。即：
        # 将根节点插入队列中；
        # 创建一个新队列，用来按顺序保存下一层的所有子节点；
        # 对于当前队列中的所有节点，按顺序依次将儿子加入新队列，并将当前节点的值记录在答案中；
        # 重复步骤2-3，直到队列为空为止。
        if not root:
            return []
        res, nodes = [], []
        nodes.append(root)
        while len(nodes) > 0:
            level = []
            for i in range(0, len(nodes)):
                r = nodes.pop(0)
                if r.left:
                    nodes.append(r.left)
                if r.right:
                    nodes.append(r.right)
                level.append(r.val)
            res.append(level)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        levels = [] 
        level = 0
        queue = deque([root])
        
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level 
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return levels