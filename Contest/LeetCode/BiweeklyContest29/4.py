# 1494. Parallel Courses II
# User Accepted:662
# User Tried:1871
# Total Accepted:739
# Total Submissions:4260
# Difficulty:Hard
# Given the integer n representing the number of courses at some university labeled from 1 to n,
# and the array dependencies where dependencies[i] = [xi, yi]  represents a prerequisite relationship,
# that is, the course xi must be taken before the course yi.  Also, you are given the integer k.
# In one semester you can take at most k courses
# as long as you have taken all the prerequisites for the courses you are taking.
# Return the minimum number of semesters to take all courses.
# It is guaranteed that you can take all courses in some way.

# Example 1:
# Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
# Output: 3 
# Explanation: The figure above represents the given graph.
# In this case we can take courses 2 and 3 in the first semester,
# then take course 1 in the second semester and finally take course 4 in the third semester.

# Example 2:
# Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
# Output: 4 
# Explanation: The figure above represents the given graph.
# In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester
# and take course 4 in the second semester,
# then take course 1 in the third semester and finally take course 5 in the fourth semester.

# Example 3:
# Input: n = 11, dependencies = [], k = 2
# Output: 6
 
# Constraints:
# 1 <= n <= 15
# 1 <= k <= n
# 0 <= dependencies.length <= n * (n-1) / 2
# dependencies[i].length == 2
# 1 <= xi, yi <= n
# xi != yi
# All prerequisite relationships are distinct, that is, dependencies[i] != dependencies[j].
# The given graph is a directed acyclic graph.

class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:

        backward = {i: set() for i in range(n)}
        forward = {i: set() for i in range(n)}
        avail = set(range(n))
        for pre, post in dependencies:
            pre -= 1
            post -= 1
            backward[post].add(pre)
            forward[pre].add(post)
            avail.discard(post)
        masks = [0] * n
        while avail:
            new_avail = set()
            for i in avail:
                for f in forward[i]:
                    masks[f] |= masks[i]
                    masks[f] |= 2 ** i
                    backward[f].remove(i)
                    if not backward[f]:
                        new_avail.add(f)
            avail = new_avail

        @functools.lru_cache(None)
        def dp(mask):
            if mask == 2 ** n - 1:
                return 0
            avail = {i for i in range(n) if (not 2 ** i & mask) and masks[i] & mask == masks[i]}
            if len(avail) <= k:
                for i in avail:
                    mask |= 2 ** i
                return 1 + dp(mask)
            ans = math.inf
            for comb in itertools.combinations(avail, k):
                diff = sum(2 ** i for i in comb)
                ans = min(ans, 1 + dp(mask | diff))
            return ans

        return dp(0)