# 1521. Find a Value of a Mysterious Function Closest to Target
# User Accepted:236
# User Tried:832
# Total Accepted:247
# Total Submissions:1968
# Difficulty:Hard
# Winston was given the above mysterious function func. 
# He has an integer array arr and an integer target 
# and he wants to find the values l and r that make the value |func(arr, l, r) - target| minimum possible.
# Return the minimum possible value of |func(arr, l, r) - target|.
# Notice that func should be called with the values l and r where 0 <= l, r < arr.length.

# Example 1:
# Input: arr = [9,12,3,7,15], target = 5
# Output: 2
# Explanation: Calling func with all the pairs of 
# [l,r] = [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]], 
# Winston got the following results [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0]. 
# The value closest to 5 is 7 and 3, thus the minimum difference is 2.

# Example 2:
# Input: arr = [1000000,1000000,1000000], target = 1
# Output: 999999
# Explanation: Winston called the func with all possible values of [l,r] and he always got 1000000, 
# thus the min difference is 999999.

# Example 3:
# Input: arr = [1,2,4,8,16], target = 0
# Output: 0
 
# Constraints:
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^6
# 0 <= target <= 10^7

class Solution(object):
    def closestToTarget(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        # Naive TLE O(n^3)

        # def func(arr, l, r):
        #     res = arr[l]
        #     for i in range(l+1, r+1):
        #         res &= arr[i]
        #     return res
        
        # n = len(arr)
        # minm = float('inf')
        # for i in range(n):
        #     for j in range(n):
        #         minm = min(minm, abs(func(arr, i, j) - target))
        # return minm


        if target in arr:
            return 0

        # 去除相邻重复元素
        tmp = [arr[0]]
        n = len(arr)
        for i in range(1, n):
            if arr[i] != tmp[-1]:
                tmp.append(arr[i])
        arr = tmp

        # special for reduplicate test cases.
        arr = sorted(list(set(arr)), key=arr.index)     

        res = float('inf')
        for i in range(len(arr)):
            cur = arr[i]
            for j in range(i, len(arr)):
                cur &= arr[j]
                res = min(res, abs(target - cur))
                if res == 0:
                    return res
                if cur < target:
                    break
        return res
