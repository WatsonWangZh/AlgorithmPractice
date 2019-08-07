# Given a binary tree
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, 
# the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# Example:
# Input: 
#     1        
#    /  \
#   2    3
#  / \    \
# 4   5    7

# Output:
#     1 -> NULL
#   /  \
#  2 -> 3 -> NULL
# / \    \
#4-> 5 -> 7 -> NULL

# Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},
# "next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,
# "right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,
# "val":7},"val":3},"val":1}

# Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,
# "next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},
# "right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},
# "val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}

# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer 
# to point to its next right node, just like in Figure B.
 
# Note:
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.

# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # BFS，树的遍历 O(n)
        # 从根节点开始宽度优先遍历，每次遍历一层，从左到右依次遍历每个节点。
        # 遍历时维护下一层节点的链表。
        # 对于每个节点，依次判断它的左儿子和右儿子是否在存在，如果存在，则插入下一层链表的末尾。
        # 时间复杂度分析：每个节点仅会遍历一次。
        # 对于每个节点，遍历时维护下一层链表的时间复杂度是 O(1)，所以总时间复杂度是 O(n)。

        if not root:
            return root
        
        levels = []
        current = [root]
        
        while current:
            levels.append(current)
            current = []
            for node in levels[-1]:
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)
                    
        for level in levels:
            for i in range(len(level) - 1):
                level[i].next = level[i+1]
                
        return root
        