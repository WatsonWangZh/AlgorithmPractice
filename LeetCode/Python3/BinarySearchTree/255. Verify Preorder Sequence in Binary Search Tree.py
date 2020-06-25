# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
# You may assume each number in the sequence is unique.
# Consider the following binary search tree: 
#      5
#     / \
#    2   6
#   / \
#  1   3

# Example 1:
# Input: [5,2,6,1,3]
# Output: false

# Example 2:
# Input: [5,2,1,3,6]
# Output: true

# Follow up:
# Could you do it using only constant space complexity?

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        # 栈的应用 O(n)
        # 先设一个最小值 minVal，
        # 然后遍历数组，如果当前值小于这个最小值 minVal，返回 false，
        # 对于根节点，将其压入栈中，然后往后遍历，
        # 如果遇到的数字比栈顶元素小，说明是其左子树的点，继续压入栈中，直到遇到的数字比栈顶元素大，那么就是右边的值了，
        # 需要找到是哪个节点的右子树，所以更新 minVal 值并删掉栈顶元素，
        # 然后继续和下一个栈顶元素比较，如果还是大于，则继续更新 minVal 值和删掉栈顶，直到栈为空或者当前栈顶元素大于当前值停止，压入当前值，
        # 这样如果遍历完整个数组之前都没有返回 false 的话，最后返回 true 即可。
        
        # stack = []
        # minVal = float('-inf')

        # for num in preorder:
        #     if num < minVal:
        #         return False

        #     while stack and num > stack[-1]:
        #         minVal = stack.pop()
        
        #     stack.append(num)

        # return True

        # 空间优化
        # 为了使空间复杂度为常量，我们不能使用 stack，
        # 所以直接修改 preorder，将 low 值存在 preorder 的特定位置即可，前提是不能影响当前的遍历。

        minVal, i = float("-inf"), -1

        for p in preorder:
            if p < minVal:
                return False

            while i >= 0 and p > preorder[i]:
                minVal = preorder[i]
                i -= 1

            i += 1
            preorder[i] = p

        return True