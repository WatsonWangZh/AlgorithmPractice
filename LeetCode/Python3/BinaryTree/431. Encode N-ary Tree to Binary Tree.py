# Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree. 
# An N-ary tree is a rooted tree in which each node has no more than N children. 
# Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. 
# There is no restriction on how your encode/decode algorithm should work. 
# You just need to ensure that an N-ary tree can be encoded to a binary tree 
# and this binary tree can be decoded to the original N-nary tree structure.
# For example, you may encode the following 3-ary tree to a binary tree in this way:
# Note that the above is just an example which might or might not work. 
# You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Note:
# N is in the range of [1, 1000]
# Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        
        :type root: Node
        :rtype: TreeNode
        """
        # https://www.cnblogs.com/grandyang/p/9945345.html
        # 左指针存第一个孩子，右指针存第一个孩子的兄弟结点
        
        if not root:
            return None

        res = TreeNode(root.val)

        if root.children:
            res.left = self.encode(root.children[0])

        cur = res.left
        for i in range(1, len(root.children)):
            cur.right = self.encode(root.children[i])
            cur = cur.right

        return res

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        
        :type data: TreeNode
        :rtype: Node
        """
        if not data:
            return None

        res = Node(data.val, [])

        cur = data.left
        while cur:
            res.children.append(self.decode(cur))
            cur = cur.right

        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))