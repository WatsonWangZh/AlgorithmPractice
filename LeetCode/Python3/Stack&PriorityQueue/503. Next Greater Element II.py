# Given a circular array (the next element of the last element is the first element of the array), 
# print the Next Greater Number for every element. 
# The Next Greater Number of a number x is the first greater number 
# to its traversing-order next in the array, which means you could search circularly 
# to find its next greater number. If it doesn't exist, output -1 for this number.

# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number; 
# The second 1's next greater number needs to search circularly, which is also 2.

# Note: The length of given array won't exceed 10000.

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # M1. 直接遍历查找 O(n^2)
        # 使用%符号来实现循环数组。 Time Limit Exceeded
        # 时间复杂度: O(n^2) 空间复杂度O(n)
        result = [-1] * len(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums) * 2):
                if nums[j % len(nums)] > nums[i]:
                    result[i] = nums[j % len(nums)]
                    break
        return result

        # M2. 单调栈 O(n)
        # 类似496题，遍历两遍原始数组，对 nums 的每个元素，可以用单调递减栈求其右边第一个比其大的元素。
        # 即如果新入栈的元素比栈顶元素要大，则栈顶出栈，直到不比栈顶元素大为止。
        # 栈顶出栈的过程中，就已经确定了其右边第一个比它大的元素就是最后要新入栈的元素。
        # 时间复杂度分析：
        # 单调栈每个元素最多进栈一次，出栈一次，故时间复杂度为O(n)。
        
        # 写法1
        stack, result = [], [-1 for _ in nums]
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                result[stack.pop()] = num
            stack.append(i)

        for num in nums:
            while len(stack) > 1 and nums[stack[-1]] < num:
                result[stack.pop()] = num
        return result
        
        # 写法2
        result = [-1] * len(nums)
        stack = []
        for i in range(len(nums)) * 2: ###### 还有这样的操作？
            while stack and (nums[stack[-1]] < nums[i]):
                result[stack.pop()] = nums[i]
            stack.append(i)

        return result
