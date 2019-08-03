# One way to serialize a binary tree is to use pre-order traversal. 
# When we encounter a non-null node, we record the node's value. If it is a null node, 
# we record using a sentinel value such as #.
#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", 
# where # represents a null node.
# Given a string of comma separated values, verify whether it is a correct 
# preorder traversal serialization of a binary tree. Find an algorithm without 
# reconstructing the tree.
# Each comma separated value in the string must be either an integer 
# or a character '#' representing null pointer.
# You may assume that the input format is always valid, 
# for example it could never contain two consecutive commas such as "1,,3".

# Example 1:
# Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true

# Example 2:
# Input: "1,#"
# Output: false

# Example 3:
# Input: "9,#,#,1"
# Output: false

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # M1. 出度入度之差 
        # 入度等于出度
        # 根节点：0个入度，2个出度；其他非空结点：1个入度，2个出度；空节点：1个入度，0个出度。
        # 应保证出度-入度始终≥0，且最终差值为0。
        # 遍历到每个结点时，因为入度为1，所以diff -= 1（考虑头结点，diff初始化为1）。
        # 如果非空，因为出度为2，所以diff += 2。

        diff = 1

        preorder = preorder.split(',')
        for x in preorder:
            diff -= 1
            if diff < 0:
                return False
            if x != '#':
                diff += 2
        return diff == 0

        # M2. 栈
        '''
        不断的砍掉叶子节点，最后看能不能全部砍掉。
        遇到x # #的时候，就把它变为 #
        “9,3,4,#,#,1,#,#,2,#,6,#,#” 为例
        模拟过程：
        9,3,4,#,# => 9,3,# 继续读
        9,3,#,1,#,# => 9,3,#,# => 9,# 继续读
        9,#2,#,6,#,# => 9,#,2,#,# => 9,#,# => # 
        '''
        preorder = preorder.split(',')
        stack = []
        for x in preorder:
            stack.append(x)
            while len(stack) >= 3 and stack[-2:] == ['#','#'] and stack[-3] != '#':
                stack[-3:] = '#'
        return stack == ['#']
        