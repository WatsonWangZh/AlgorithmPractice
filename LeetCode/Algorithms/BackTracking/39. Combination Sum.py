# Given a set of candidate numbers (candidates) (without duplicates) 
# and a target number (target), 
# find all unique combinations in candidates 
# where the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]

# Example 2:
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

class Solution(object):
    def combinationSum(self, candidates, target):
        # if not candidates:
        #     return
        # res = [[] for i in range(len(candidates))]
        # for i in range(len(candidates)):
        #     if target % candidates[i] == 0:
        #         times = target // candidates[i]
        #         res.
        result = []
        candidates = sorted(candidates)
        self.cs_dfs(candidates, target, 0, [],result)
        return result
    
    def cs_dfs(self, nums, current_remain, start_index, current_res, res):
        if current_remain == 0:
            return res.append(current_res)
        for i in range(start_index, len(nums)):
            if nums[i] > current_remain:
                break
            else:
                self.cs_dfs(nums, current_remain-nums[i], i, current_res+[nums[i]], res)

def main():
    s = Solution()
    print(s.combinationSum(candidates = [2,3,6,7], target = 7))
    print(s.combinationSum(candidates = [2,3,5], target = 8))

if __name__ == "__main__":
    main()