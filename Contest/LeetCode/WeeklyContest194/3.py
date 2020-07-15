# 1488. Avoid Flood in The City
# User Accepted:1202
# User Tried:3504
# Total Accepted:1240
# Total Submissions:11201
# Difficulty:Medium
# Your country has an infinite number of lakes. Initially, all the lakes are empty,
# but when it rains over the nth lake, the nth lake becomes full of water.
# If it rains over a lake which is full of water,
# there will be a flood. Your goal is to avoid the flood in any lake.
# Given an integer array rains where:
# rains[i] > 0 means there will be rains over the rains[i] lake.
# rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
# Return an array ans where:
# ans.length == rains.length
# ans[i] == -1 if rains[i] > 0.
# ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
# If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.
# Notice that if you chose to dry a full lake, it becomes empty,
# but if you chose to dry an empty lake, nothing changes. (see example 4)

# Example 1:
# Input: rains = [1,2,3,4]
# Output: [-1,-1,-1,-1]
# Explanation: After the first day full lakes are [1]
# After the second day full lakes are [1,2]
# After the third day full lakes are [1,2,3]
# After the fourth day full lakes are [1,2,3,4]
# There's no day to dry any lake and there is no flood in any lake.

# Example 2:
# Input: rains = [1,2,0,0,2,1]
# Output: [-1,-1,2,1,-1,-1]
# Explanation: After the first day full lakes are [1]
# After the second day full lakes are [1,2]
# After the third day, we dry lake 2. Full lakes are [1]
# After the fourth day, we dry lake 1. There is no full lakes.
# After the fifth day, full lakes are [2].
# After the sixth day, full lakes are [1,2].
# It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.

# Example 3:
# Input: rains = [1,2,0,1,2]
# Output: []
# Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
# After that, it will rain over lakes [1,2].
# It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.

# Example 4:
# Input: rains = [69,0,0,0,69]
# Output: [-1,69,1,1,-1]
# Explanation: Any solution on one of the forms
# [-1,69,x,y,-1], [-1,x,69,y,-1] or [-1,x,y,69,-1] is acceptable where 1 <= x,y <= 10^9

# Example 5:
# Input: rains = [10,20,20]
# Output: []
# Explanation: It will rain over lake 20 two consecutive days. There is no chance to dry any lake.
 
# Constraints:
# 1 <= rains.length <= 10^5
# 0 <= rains[i] <= 10^9

# Total Wrong Thought. WA.
# from collections import defaultdict, Counter
# import random
# import heapq
# class Solution:
#     def avoidFlood(self, rains: List[int]) -> List[int]:
#         res = [-2] * len(rains)
#         fulled = defaultdict(bool)
#         dic = []
#         count = Counter(rains).most_common()
#
#         for i, rain in enumerate(rains):
#             # print(fulled, rain, res, dic)
#             if fulled[rain]:
#                 return []
#             if rain > 0:
#                 res[i] = -1
#                 fulled[rain] = True
#                 dic.append(rain)
#             if rain == 0:
#                 can = Counter(rains[i:]).most_common()[0]
#                 if can in dic:
#                     dic.remove(can)
#                     res[i] = can
#                     fulled[can] = False
#                 else:
#                     res[i] = random.choice(dic) if len(dic) else 1
#                     if res[i] in dic:
#                         dic.remove(res[i])
#                     fulled[res[i]] = False
#         return res


# 预处理 贪心
class pair():
    def __init__(self, nextrainday, poolid):
        self.nextrainday = nextrainday
        self.poolid = poolid

    def __lt__(self, other):
        if self.nextrainday < other.nextrainday:
            return True
        else:
            return False

    def info(self):
        print(self.nextrainday, self.poolid)


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        nxt = [n + 1] * n
        time = defaultdict(int)
        for i in range(n - 1, -1, -1):
            # print(time, nxt)
            r = rains[i]
            if r:
                if r in time.keys():
                    nxt[i] = time[r]
                time[r] = i + 1
        # print(time, nxt)

        heap = []
        res = []
        isfull = defaultdict(bool)
        for i in range(n):
            r = rains[i]
            if r:
                if isfull[r]:
                    # print('damn it')
                    return []
                isfull[r] = True
                heapq.heappush(heap, pair(nxt[i], r))
                res.append(-1)
            else:
                if not heap:
                    res.append(1)
                else:
                    t = heapq.heappop(heap)
                    isfull[t.poolid] = False
                    res.append(t.poolid)
        return res