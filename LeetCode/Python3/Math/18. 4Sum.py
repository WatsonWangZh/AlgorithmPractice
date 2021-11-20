# Given an array nums of n integers and an integer target, 
# are there elements a, b, c, and d in nums such that a + b + c + d = target? 
# Find all unique quadruplets in the array which gives the sum of target.
# Note:
# The solution set must not contain duplicate quadruplets.
# Example:
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) < 4 or nums[0] * 4 >target or nums[-1] * 4 <target:
            return []
        res = []
        for first in range(len(nums) - 3):
            if first and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, len(nums) - 2):
                if second != first + 1 and nums[second] == nums[second - 1]:
                    continue
                sum = target - nums[first] - nums[second]
                third, forth = second + 1, len(nums) - 1
                while third < forth:
                    if nums[third] + nums[forth] == sum:
                        res.append([nums[first], nums[second], nums[third], nums[forth]])
                        forth -= 1
                        third += 1
                        while third < forth and nums[third] == nums[third - 1]:
                            third += 1
                        while third < forth and nums[forth] == nums[forth + 1]:
                            forth -= 1
                    elif nums[third] + nums[forth] > sum:
                        forth -= 1
                    else:
                        third += 1
        return res 


def main():
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2],0))

if __name__ == '__main__': 
    main()   