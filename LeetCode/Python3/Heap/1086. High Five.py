# Given a list of scores of different students, 
# return the average score of each student's top five scores in the order of each student's id.
# Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  
# The average score is calculated using integer division.

# Example 1:
# Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation: 
# The average of the student with id = 1 is 87.
# The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
 
# Note:
# 1 <= items.length <= 1000
# items[i].length == 2
# The IDs of the students is between 1 to 1000
# The score of the students is between 1 to 100
# For each student, there are at least 5 scores

# Hints:
# How can we solve the problem if we have just one student?
# Given an student sort their grades and get the top 5 average.
# Generalize the idea to do it for many students.

import heapq
from collections import defaultdict
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        # 大根堆
        # 给每个学生一个大根堆，把其所有的成绩都放入堆中，最后堆中最大的5个数字就是最高的5科成绩。

        res = []
        data = defaultdict(list)
        for id, score in items:
            heapq.heappush(data[id], score)
            
        for id, scores in data.items():
            avg = sum(heapq.nlargest(5, scores)) // 5
            res.append((id, avg))
        return res