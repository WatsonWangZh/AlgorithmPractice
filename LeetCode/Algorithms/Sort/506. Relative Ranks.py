# Given scores of N athletes, 
# find their relative ranks and the people with the top three highest scores, 
# who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

# Example 1:
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, 
# so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
# For the left two athletes, you just need to output their relative ranks according to their scores.

# Note:
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # 排序查表 分别处理 O(nlgn)
        ranks = {}
        for idx,num in enumerate(sorted(nums, reverse = True)):
            ranks[num] = idx
            
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        res = []
        for num in nums:
            if ranks[num] < 3:
                res.append(medals[ranks[num]])
            else:
                res.append(str(ranks[num]+1))
        return res