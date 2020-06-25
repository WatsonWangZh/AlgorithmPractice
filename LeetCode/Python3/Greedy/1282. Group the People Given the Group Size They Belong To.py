# There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. 
# Given the array groupSizes of length n telling the group size each person belongs to, 
# return the groups there are and the people's IDs each group includes.
# You can return any solution in any order and the same applies for IDs. 
# Also, it is guaranteed that there exists at least one solution. 

# Example 1:
# Input: groupSizes = [3,3,3,3,3,1,3]
# Output: [[5],[0,1,2],[3,4,6]]
# Explanation: 
# Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

# Example 2:
# Input: groupSizes = [2,1,3,3,3,2]
# Output: [[1],[0,5],[2,3,4]]
 
# Constraints:
# groupSizes.length == n
# 1 <= n <= 500
# 1 <= groupSizes[i] <= n

# Hints:
# Put people's IDs with same groupSize into buckets, then split each bucket into groups.
# Greedy fill until you need a new group.

class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        # 分组 贪心分配
        res = []
        temp = collections.defaultdict(list)
        for i in range(len(groupSizes)):
            temp[groupSizes[i]].append(i)
            if len(temp[groupSizes[i]]) == groupSizes[i]:
                res.append(temp[groupSizes[i]])
                del temp[groupSizes[i]]
        return res