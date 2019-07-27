# Given a collection of numbers that might contain duplicates, 
# return all possible unique permutations.

# Example:
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        visited = [False] * len(nums)
        # 1
        self.dfs(sorted(nums), 0, temp, res, visited)

        return res

    def dfs(self, nums, pos, temp, res, visited):
        if pos == len(nums):
            res.append(temp[:])
            return 

        for i in range(len(nums)):
            # 2
            if i > 0 and nums[i] == nums[i-1] and visited[i-1]:
                continue

            if not visited[i]:
                visited[i] = True
                temp.append(nums[i])
                self.dfs(nums, pos+1, temp, res, visited)
                visited[i] = False
                temp.pop()
