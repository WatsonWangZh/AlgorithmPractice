# Given a set of N people (numbered 1, 2, ..., N), 
# we would like to split everyone into two groups of any size.
# Each person may dislike some other people, and they should not go into the same group. 
# Formally, if dislikes[i] = [a, b], 
# it means it is not allowed to put the people numbered a and b into the same group.
# Return true if and only if it is possible to split everyone into two groups in this way.

# Example 1:
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]

# Example 2:
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false

# Example 3:
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
 
# Note:
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].

import collections
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        graph = collections.defaultdict(list)
        for dislike in dislikes:
            graph[dislike[0] - 1].append(dislike[1] - 1)
            graph[dislike[1] - 1].append(dislike[0] - 1)

        color = [0] * N
        for i in range(N):
            if color[i] != 0: 
                continue
            dfs = collections.deque()
            dfs.append(i)
            color[i] = 1
            
            while dfs:
                cur = dfs.popleft()
                for e in graph[cur]:
                    if color[e] != 0:
                        if color[cur] == color[e]:
                            return False
                    else:
                        color[e] = -color[cur]
                        dfs.append(e)
        return True