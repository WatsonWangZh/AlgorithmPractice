# Serialization is the process of converting a data structure or object into a sequence of bits 
# so that it can be stored in a file or memory buffer, 
# or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize an N-ary tree. 
# An N-ary tree is a rooted tree in which each node has no more than N children. 
# There is no restriction on how your serialization/deserialization algorithm should work. 
# You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# For example, you may serialize the following 3-ary tree
# as [1 [3[5 6] 2 4]]. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Note:
# N is in the range of [1, 1000]
# Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Codec:
    # https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/359037/Python-Recursive-solution-without-queue-or-stack
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: Node
        :rtype: str
        """
        nodeList = []
        self.serializeHelper(root, nodeList)
        # print(map(str, nodeList))
        return ','.join(map(str, nodeList))


    def serializeHelper(self, root, nodeList):
        if root is None:
            return
        nodeList.append(root.val)
        nodeList.append(len(root.children))
        for child in root.children:
            self.serializeHelper(child, nodeList)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: Node
        """
        if len(data) <= 0:
            return None
        nodeList = data.split(",")
        indexs = [0]
        deserializedData = self.deserializeHelper(nodeList, indexs)
        return deserializedData


    def deserializeHelper(self, nodeList, indexs):
        if indexs[0] == len(nodeList):
            return None
        root = Node(int(nodeList[indexs[0]]), [])
        indexs[0] += 1
        childrenSize = int(nodeList[indexs[0]])
        indexs[0] += 1
        for index in range(childrenSize):
            root.children.append(self.deserializeHelper(nodeList, indexs))
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))