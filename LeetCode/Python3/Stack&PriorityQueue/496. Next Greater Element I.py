# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. 
# If it does not exist, output -1 for this number.

# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
#     For number 4 in the first array, 
#     you cannot find the next greater number for it in the second array, so output -1.
#     For number 1 in the first array, the next greater number for it in the second array is 3.
#     For number 2 in the first array, there is no next greater number for it in the second array, 
#     so output -1.

# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
#     For number 2 in the first array, the next greater number for it in the second array is 3.
#     For number 4 in the first array, there is no next greater number for it in the second array, 
#     so output -1.
# Note:
# All elements in nums1 and nums2 are unique.
# The length of both nums1 and nums2 would not exceed 1000.

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # M1. 直接遍历查找
        # 先从nums2中找到对应的nums1数值的序号，然后从这个序号往又找，看有没有比nums1数字大的。
        # 如果有，把这个数字放到结果里；如果没有，就把-1放到结果里。
        # res = []
        # for num1 in nums1:
        #     index = -1
        #     for i,num2 in enumerate(nums2):
        #         if num1 == nums2[i]:
        #             index = i
        #             break
        #     while index < len(nums2) and num1 >= nums2[index]:
        #         index += 1
        #     if index == len(nums2):
        #         res.append(-1)
        #     else:
        #         res.append(nums2[index])            
        # return res
        
        # M2. 单调栈 + hashmap O(n)
        # 先用一个单调递减的栈来算出每个数的下一个较大值，
        # 如果新加进栈的元素比栈顶元素大，说明当前新加的元素就是当前栈顶元素的下一个较大值，
        # 然后把这个关系存到hashmap里面，找好下一个较大值的从栈里pop出来，把新的元素再放到栈里面。
        # 最后，遍历nums1, 把里面每个元素的对应结果从hash表里取出来。

        maps = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                maps[stack.pop()] = num
            stack.append(num)
        
        res = []
        for num in nums1:
            res.append(maps[num] if num in maps else -1)
        return res
        