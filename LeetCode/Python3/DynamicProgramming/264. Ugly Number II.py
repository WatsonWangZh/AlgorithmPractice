# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 
# is the sequence of the first 10 ugly numbers.

# Note:  
# 1 is typically treated as an ugly number.
# n does not exceed 1690.

# Hints:
# The naive approach is to call isUgly for every number until you reach the nth one. 
# Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
# An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
# The key is how to maintain the order of the ugly numbers. 
# Try a similar approach of merging from three sorted lists: L1, L2, and L3.
# Assume you have Uk, the kth ugly number. 
# Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # M1. 最小堆 O(nlogn)
        # 考虑到第n个丑数一定是由前面的丑数乘上2或3或5得到的，
        # 因此可以通过对每个丑数依次乘上2、3、5得到后面的丑数，
        # 在这里采用最小堆实现。维护一个最小堆，使得最小堆中的数一定是丑数。
        # 首先初始化堆，将1放入堆中，之后循环n次，
        # 对于第i次，利用最小堆弹出最小的数，即第i大的丑数，
        # 然后对该数乘上2、3、5得到之后的丑数放入堆中，以此类推。
        # 时间复杂度分析：
        # 每轮需要从堆中弹出堆顶并插入新的数，因此每一轮复杂度为O(logn)，需要循环n轮，
        # 所以复杂度为O(nlogn)。

        # import heapq
        # heap = [1]
        # heapq.heapify(heap)
        # lastnum = -1
        # i = 0
        # while i < n:
        #     top = heapq.heappop(heap)
        #     if top == lastnum:
        #         continue
        #     heapq.heappush(heap, top * 2)
        #     heapq.heappush(heap, top * 3)
        #     heapq.heappush(heap, top * 5)
        #     lastnum = top
        #     i += 1
        # return top

        # M2. 动态规划 指针 O(n)
        # 由于丑数的因子也必定是丑数，它一定是某个丑数乘2、3、5得到的，
        # 因此我们可以采用动态规划的思想，利用前面已经得到的丑数序列来得到之后的丑数，
        # 而问题的关键在于如何确定状态转移方程。由于小的丑数乘5不一定比大的丑数乘2要小，
        # 我们没法直接使用目前最大的丑数来乘2、3、5顺序得到更大的丑数。
        # 不过，我们可以确定的是，小的丑陋数乘2，肯定小于大的丑陋数乘2。
        # 所以我们使用三个指针，分别记录乘2、3、5得出的目前最大丑陋数，
        # 而新的丑数就是这三个目前最大丑数中最小的那个，那么就需要更新被选中的丑数的指针，
        # 获得新的三个目前最大丑数，依次类推，从而得到最终结果。
        # 时间复杂度分析：
        # 需要维护3个指针，从1到n遍历，复杂度为O(n)。

        ugly = []
        ugly.append(1)
        i2, i3, i5 = 0, 0, 0
        while(len(ugly) <= n):
            while(ugly[i2] * 2 <= ugly[-1]):
                i2 +=1
            while(ugly[i3] * 3 <= ugly[-1]):
                i3 +=1
            while(ugly[i5] * 5 <= ugly[-1]):
                i5 +=1 
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[n-1]
