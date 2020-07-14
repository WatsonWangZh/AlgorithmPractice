# 5454. Least Number of Unique Integers after K Removals
# User Accepted:6303
# User Tried:6983
# Total Accepted:6453
# Total Submissions:12682
# Difficulty:Medium
# Given an array of integers arr and an integer k.
# Find the least number of unique integers after removing exactly k elements.

# Example 1:
# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.

# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 
# Constraints:
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^9
# 0 <= k <= arr.length

from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        most_common = Counter(arr).most_common()
        most_common.sort(key=lambda x: x[1])

        while k > 0:
            for i, tup in enumerate(most_common):
                k -= tup[1]
                if k < 0:
                    break
                tup = tup[:1] + (0,)
                most_common[i] = tup

        res = 0
        for _, val in most_common:
            if val > 0:
                res += 1
        return res

        # Counter计数 排序
        dic = Counter(int)
        for x in arr:
            dic[x] += 1

        cnt = []
        for x in dic.keys():
            cnt.append(dic[x])
        cnt.sort()

        res = len(cnt)
        for c in cnt:
            if k >= c:
                k -= c
                res -= 1
            else:
                break
        return res