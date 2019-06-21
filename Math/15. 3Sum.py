# Given an array nums of n integers, 
# are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.

# Note:
# The solution set must not contain duplicate triplets.

# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
     def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """

    #     nums.sort()        
    #     if len(nums) < 3 or nums[-1] < 0 or nums[0] > 0:
    #         return []
    #     res = []
    #     first_pos = 0     
    #     while first_pos < len(nums)-2 :
    #         if first_pos == 0 or nums[first_pos] != nums[first_pos-1]:
    #             second_pos , third_pos = first_pos + 1 , len(nums)-1
    #             while second_pos < third_pos:
    #                 if nums[first_pos] + nums[second_pos] + nums[third_pos] < 0:
    #                     second_pos += 1
    #                 elif nums[first_pos] + nums[second_pos] + nums[third_pos] > 0:
    #                     third_pos -= 1
    #                 else:
    #                     res.append([nums[first_pos],nums[second_pos],nums[third_pos]])
    #                     second_pos , third_pos = second_pos + 1,third_pos -1
    #                     if nums[second_pos] == nums[second_pos-1]:
    #                         second_pos += 1
    #                     if nums[third_pos] == nums[third_pos+1]:
    #                         third_pos -= 1
    #         first_pos += 1
    #     return res

    #大佬代码
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        if 0 in counter and counter[0] > 2:
            rst = [[0,0,0]]
        else:
            rst = []
        
        uniques = counter.keys()
        pos = sorted(p for p in uniques if p > 0)
        neg = sorted(n for n in uniques if n < 0)
        
        for p in pos:
            for n in neg:
                inverse = -(p+n)
                if inverse in counter:
                    if inverse == p and counter[p] > 1:
                        rst.append([n,p,p])
                    elif inverse == n and counter[n] > 1:
                        rst.append([n,n,p])
                    elif n<inverse< p or inverse == 0:
                        rst.append([n,inverse,p])
        return rst


def main():
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))

if __name__ == '__main__': 
    main()