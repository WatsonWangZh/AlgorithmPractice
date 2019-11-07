# There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

# Now we want to hire exactly K workers to form a paid group.  
# When hiring a group of K workers, we must pay them according to the following rules:
# Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
# Every worker in the paid group must be paid at least their minimum wage expectation.
# Return the least amount of money needed to form a paid group satisfying the above conditions.

# Example 1:
# Input: quality = [10,20,5], wage = [70,50,30], K = 2
# Output: 105.00000
# Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.

# Example 2:
# Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
# Output: 30.66667
# Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 
 
# Note:
# 1 <= K <= N <= 10000, where N = quality.length = wage.length
# 1 <= quality[i] <= 10000
# 1 <= wage[i] <= 10000
# Answers within 10^-5 of the correct answer will be considered correct.

import heapq
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        # 贪心 最大堆O(nlogn)
        # 根据所有人的性价比进行倒序排序。
        # 排序后，选定第 i 个人作为 base 发工资时，1 到 i−1 的人的工资最低标准总能被满足。
        # 枚举每个人作为 base，当枚举到第 i 个人时，我们期望发的工资最少，此时工资总和与质量有关，
        # 所以我们在前 i−1 个人中选取质量最低的 K 个人，即可获得以第 i 个人为 base 时的最低工资总和。
        # 用堆来维护质量最低的 K 个人，同时用一个变量来记录此时堆中所有人的质量总和。
        # 时间复杂度
        # 排序需要 O(nlogn) 的时间。
        # 枚举 n 个人，每次枚举寻找最大值时间复杂度为常数，
        # 弹出质量最高的人并将第 i 个人插入堆中的时间复杂度为 O(logK)。
        # 故总时间复杂度为  O(nlogn) 。

        workers = sorted([(float(w)/q, q) for w, q in zip(wage, quality)])
        res = float('inf')
        qSum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qSum += q
            if len(heap) == K:
                res = min(res, qSum * r)
                qSum += heapq.heappop(heap)    # 弹出需求工资最大的
        return res
