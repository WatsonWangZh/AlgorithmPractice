# You are given a perfect binary tree where all leaves are on the same level, 
# and every parent has two children. The binary tree has the following definition:
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. 
# If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# Example:
# Input: 
#      1        
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7

# Output:
#     1 -> NULL
#   /    \
#  2  ->  3 -> NULL
# / \     / \
#4-> 5-> 6-> 7 -> NULL

# Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},
# "next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,
# "right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},
# "next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

# Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,
# "next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},
# "right":null,"val":6},"right":null,"val":5},"right":null,"val":4},
# "next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},
# "right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

# Explanation: Given the above perfect binary tree (Figure A), your function should populate each 
# next pointer to point to its next right node, just like in Figure B.
 
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
        # 从根节点开始宽度优先遍历，每次遍历一层，遍历时按从左到右的顺序，
        # 对于每个节点，先让左儿子指向右儿子，然后让右儿子指向下一个节点的左儿子。最后让这一层最右侧的节点指向NULL。
        # 遍历到叶节点所在的层为止。
        # 时间复杂度分析：每个节点仅会遍历一次，遍历时修改指针的时间复杂度是 O(1)，所以总时间复杂度是 O(n)。
        
        if not root:
            return root

        root.next = None
        leftmost = root

        while leftmost.left:
            cur = leftmost
            leftmost = cur.left
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                else:
                    cur.right.next = None
                cur = cur.next

        return root
        